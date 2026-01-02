import streamlit as st
import os
import tempfile
import geometry
import costs
import data_loader
import pandas as pd
from utils import export

print("DEBUG: Geometry imported successfully")
print("DEBUG: Costs imported successfully")
print("DEBUG: Export imported successfully")

st.set_page_config(page_title="QuoteForge", layout="wide")

st.title("QuoteForge 🛠️")
st.markdown("### Manufacturing Cost Estimator")

# Placeholder for sidebar
with st.sidebar:
    st.header("Settings")
    st.info("Configuration options will appear here.")

# Placeholder for main content
tab1, tab2, tab3, tab4 = st.tabs(["Import", "Configuration", "Costing", "Export"])

with tab1:
    st.header("Import")

    # Initialize session state for uploaded files
    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []

    # File uploader
    uploaded_files = st.file_uploader(
        "Upload STEP Files",
        type=["stp", "step"],
        accept_multiple_files=True,
        key="file_uploader",
    )

    # Process newly uploaded files
    if uploaded_files:
        for uploaded_file in uploaded_files:
            # Check if file already exists in session state
            existing_names = [f["name"] for f in st.session_state.uploaded_files]
            if uploaded_file.name not in existing_names:
                # Save to temporary location
                with tempfile.NamedTemporaryFile(delete=False, suffix=".step") as tmp:
                    tmp.write(uploaded_file.getvalue())
                    tmp_path = tmp.name

                # Store file info in session state
                st.session_state.uploaded_files.append(
                    {
                        "name": uploaded_file.name,
                        "path": tmp_path,
                        "size": uploaded_file.size,
                    }
                )

        st.success(f"Added {len(uploaded_files)} file(s)")


with tab2:
    st.header("Configuration")

    if not st.session_state.uploaded_files:
        st.warning("No files imported. Please import files in the Import tab first.")
    else:
        # Initialize configuration in session state if needed
        if "part_configs" not in st.session_state:
            st.session_state.part_configs = {}
            for file_info in st.session_state.uploaded_files:
                part_number = file_info["name"]
                st.session_state.part_configs[part_number] = {
                    "quantity": 1,
                    "material": None,
                    "cutting": None,
                    "machining": False,
                    "turning": False,
                    "3d_printing": False,
                    "forming": False,
                    "threading": False,
                    "welding": False,
                    "finishing": None,
                }

        # Load materials and processes
        materials_df = data_loader.get_materials()
        processes_df = data_loader.get_processes()

        # Categorize processes
        cutting_processes = processes_df[processes_df["category"] == "Cutting"][
            "name"
        ].tolist()
        machining_processes = processes_df[processes_df["category"] == "Machining"][
            "name"
        ].tolist()
        fabrication_processes = processes_df[processes_df["category"] == "Fabrication"][
            "name"
        ].tolist()
        finishing_processes = processes_df[processes_df["category"] == "Finishing"][
            "name"
        ].tolist()

        material_names = materials_df["name"].tolist()

        # Add custom CSS for horizontal scroll with minimum width
        st.markdown(
            """
            <style>
            .config-table-container {
                overflow-x: auto;
                width: 100%;
                min-width: 100%;
            }
            .config-table-content {
                min-width: 1600px;
                width: max-content;
            }
            /* Force column containers to not shrink */
            div[data-testid="column"] {
                min-width: fit-content !important;
            }
            </style>
        """,
            unsafe_allow_html=True,
        )

        # Start scrollable container with minimum width
        st.markdown(
            '<div class="config-table-container"><div class="config-table-content">',
            unsafe_allow_html=True,
        )

        # Create header row with fixed widths (in pixels)
        # Total width: ~1500px to ensure horizontal scroll on smaller screens
        header_cols = st.columns(
            [80, 180, 80, 200, 150, 100, 100, 100, 100, 100, 100, 150]
        )
        header_cols[0].markdown("**Thumbnail**")
        header_cols[1].markdown("**Part Number**")
        header_cols[2].markdown("**Quantity**")
        header_cols[3].markdown("**Material**")
        header_cols[4].markdown("**Cutting**")
        header_cols[5].markdown(
            "<div style='text-align: center'><strong>Machining</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[6].markdown(
            "<div style='text-align: center'><strong>Turning</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[7].markdown(
            "<div style='text-align: center'><strong>3D Printing</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[8].markdown(
            "<div style='text-align: center'><strong>Forming</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[9].markdown(
            "<div style='text-align: center'><strong>Threading</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[10].markdown(
            "<div style='text-align: center'><strong>Welding</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[11].markdown("**Finishing**")

        st.divider()

        # Create rows for each part
        for idx, file_info in enumerate(st.session_state.uploaded_files):
            part_number = file_info["name"]
            display_name = os.path.splitext(part_number)[0].replace("_", "-")

            # Ensure this part has a config
            if part_number not in st.session_state.part_configs:
                st.session_state.part_configs[part_number] = {
                    "quantity": 1,
                    "material": None,
                    "cutting": None,
                    "machining": False,
                    "turning": False,
                    "3d_printing": False,
                    "forming": False,
                    "threading": False,
                    "welding": False,
                    "finishing": None,
                }

            config = st.session_state.part_configs[part_number]

            cols = st.columns(
                [80, 180, 80, 200, 150, 100, 100, 100, 100, 100, 100, 150]
            )

            with cols[0]:
                st.text("🖼️")  # Placeholder for thumbnail

            with cols[1]:
                st.text(display_name)

            with cols[2]:
                quantity = st.number_input(
                    "Qty",
                    min_value=1,
                    value=config["quantity"],
                    key=f"qty_{idx}",
                    label_visibility="collapsed",
                )
                config["quantity"] = quantity

            with cols[3]:
                material_index = (
                    material_names.index(config["material"])
                    if config["material"] in material_names
                    else 0
                )
                material = st.selectbox(
                    "Material",
                    options=material_names,
                    index=material_index,
                    key=f"mat_{idx}",
                    label_visibility="collapsed",
                )
                config["material"] = material

            with cols[4]:
                cutting_options = ["None"] + cutting_processes
                cutting_index = (
                    cutting_options.index(config["cutting"])
                    if config["cutting"] in cutting_options
                    else 0
                )
                cutting = st.selectbox(
                    "Cutting",
                    options=cutting_options,
                    index=cutting_index,
                    key=f"cut_{idx}",
                    label_visibility="collapsed",
                )
                config["cutting"] = cutting if cutting != "None" else None

            with cols[5]:
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                machining = st.checkbox(
                    "Machining",
                    value=config["machining"],
                    key=f"mach_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["machining"] = machining

            with cols[6]:
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                turning = st.checkbox(
                    "Turning",
                    value=config["turning"],
                    key=f"turn_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["turning"] = turning

            with cols[7]:
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                printing_3d = st.checkbox(
                    "3D Printing",
                    value=config["3d_printing"],
                    key=f"3dprint_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["3d_printing"] = printing_3d

            with cols[8]:
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                forming = st.checkbox(
                    "Forming",
                    value=config["forming"],
                    key=f"form_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["forming"] = forming

            with cols[9]:
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                threading = st.checkbox(
                    "Threading",
                    value=config["threading"],
                    key=f"thread_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["threading"] = threading

            with cols[10]:
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                welding = st.checkbox(
                    "Welding",
                    value=config["welding"],
                    key=f"weld_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["welding"] = welding

            with cols[11]:
                finishing_options = ["None"] + finishing_processes
                finishing_index = (
                    finishing_options.index(config["finishing"])
                    if config["finishing"] in finishing_options
                    else 0
                )
                finishing = st.selectbox(
                    "Finishing",
                    options=finishing_options,
                    index=finishing_index,
                    key=f"finish_{idx}",
                    label_visibility="collapsed",
                )
                config["finishing"] = finishing if finishing != "None" else None

            st.divider()

        # Close scrollable container (both inner and outer divs)
        st.markdown("</div></div>", unsafe_allow_html=True)

with tab3:
    st.header("Costing")

    if not st.session_state.uploaded_files:
        st.warning("No files imported. Please import files in the Import tab first.")
    elif "part_configs" not in st.session_state or not st.session_state.part_configs:
        st.warning(
            "No configurations set. Please configure parts in the Configuration tab first."
        )
    else:
        # Load process data for cost calculations
        processes_df = data_loader.get_processes()

        grand_total = 0.0

        # Process each part
        for file_info in st.session_state.uploaded_files:
            part_number = file_info["name"]
            display_name = os.path.splitext(part_number)[0].replace("_", "-")
            file_path = file_info["path"]

            # Get configuration for this part
            config = st.session_state.part_configs.get(part_number, {})
            quantity = config.get("quantity", 1)
            material_name = config.get("material")

            # Calculate geometry (volume) for weight
            try:
                analyzer = geometry.GeometryAnalyzer(file_path)
                volume_in3 = analyzer.get_volume()
            except Exception as e:
                volume_in3 = 0.0
                st.error(f"Error analyzing {part_number}: {e}")

            # Get material info for weight calculation
            weight_lbs = 0.0
            density = 0.0
            material_cost_per_lb = 0.0

            if material_name:
                mat_info = costs.get_material_rate(material_name)
                if mat_info:
                    density = mat_info[0]
                    material_cost_per_lb = mat_info[1]
                    weight_lbs = volume_in3 * density

            # Prepare breakdown list
            cost_details = []

            # Material cost
            material_cost_single = 0.0
            material_cost_batch = 0.0
            if material_name and weight_lbs > 0:
                material_cost_single = weight_lbs * material_cost_per_lb
                material_cost_batch = material_cost_single * quantity
                cost_details.append(
                    {
                        "Process": f"Material: {material_name}",
                        "Rate": f"${material_cost_per_lb:.2f}/lbs",
                        "Setup Time": "-",
                        "Run time": "-",
                        "Single Part Cost": f"${material_cost_single:.2f}",
                        "Batch Total": f"${material_cost_batch:.2f}",
                    }
                )

            # Calculate process costs
            batch_total_process_cost = 0.0

            # Helper for process row addition
            def add_process_row(p_name, p_info):
                setup_mins = p_info[0]
                rate = p_info[1]
                run_mins = 60.0  # Default to 60 mins for now

                setup_cost = (setup_mins * rate) / 60.0
                run_cost_single = (run_mins * rate) / 60.0
                run_cost_batch = run_cost_single * quantity

                single_cost = setup_cost + run_cost_single
                batch_cost = setup_cost + run_cost_batch

                cost_details.append(
                    {
                        "Process": p_name,
                        "Rate": f"${rate:.2f}/hr",
                        "Setup Time": f"{setup_mins} mins (${setup_cost:.2f})",
                        "Run time": f"{run_mins} mins (${run_cost_single:.2f})",
                        "Single Part Cost": f"${single_cost:.2f}",
                        "Batch Total": f"${batch_cost:.2f}",
                    }
                )
                return batch_cost

            # Cutting process
            cutting = config.get("cutting")
            if cutting:
                proc_info = costs.get_process_rates(cutting)
                if proc_info:
                    batch_total_process_cost += add_process_row(cutting, proc_info)

            # Checkbox processes
            checkbox_processes = [
                ("machining", "Machining"),
                ("turning", "Turning"),
                ("3d_printing", "3D Printing"),
                ("forming", "Forming"),
                ("threading", "Threading"),
                ("welding", "Welding"),
            ]

            for config_key, process_name in checkbox_processes:
                if config.get(config_key, False):
                    proc_info = costs.get_process_rates(process_name)
                    if proc_info:
                        batch_total_process_cost += add_process_row(
                            process_name, proc_info
                        )

            # Finishing process
            finishing = config.get("finishing")
            if finishing:
                proc_info = costs.get_process_rates(finishing)
                if proc_info:
                    batch_total_process_cost += add_process_row(finishing, proc_info)

            total_cost = material_cost_batch + batch_total_process_cost
            per_part_cost = total_cost / quantity if quantity > 0 else 0
            grand_total += total_cost

            # Render Card
            with st.container(border=True):
                col_img, col_info, col_toggle = st.columns(
                    [1, 4, 0.1]
                )  # Adjusted for simple expander later

                with col_img:
                    st.text("🖼️")  # Thumbnail placeholder holder
                    st.caption("Thumbnail")

                with col_info:
                    st.subheader(display_name)

                    metric_cols = st.columns(4)
                    metric_cols[0].metric("Weight", f"{weight_lbs:.2f} lbs")
                    metric_cols[1].metric("Quantity", str(quantity))
                    metric_cols[2].metric("Per Part Cost", f"${per_part_cost:.2f}")
                    metric_cols[3].metric("Total Cost", f"${total_cost:.2f}")

                # Details Expander
                with st.expander("Cost Breakdown"):
                    if cost_details:
                        df = pd.DataFrame(cost_details)
                        st.table(
                            df
                        )  # Using st.table for full view as per requirement "small table"
                    else:
                        st.info("No costs associated.")
        # Grand total
        st.markdown(f"### Grand Total: **${grand_total:.2f}**")

with tab4:
    st.header("Export")
    st.info("Export functionality will be implemented here.")
