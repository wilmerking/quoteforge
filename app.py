import streamlit as st
import os
import tempfile
import geometry
import costs
import data_loader
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

    # Display uploaded files
    if st.session_state.uploaded_files:
        st.subheader(f"Imported Files ({len(st.session_state.uploaded_files)})")

        for idx, file_info in enumerate(st.session_state.uploaded_files):
            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:
                st.text(file_info["name"])

            with col2:
                # Display file size in KB
                size_kb = file_info["size"] / 1024
                st.text(f"{size_kb:.2f} KB")

            with col3:
                if st.button("Remove", key=f"remove_{idx}"):
                    # Delete the temporary file
                    try:
                        os.remove(file_info["path"])
                    except:
                        pass  # File may already be deleted

                    # Remove from session state
                    st.session_state.uploaded_files.pop(idx)
                    st.rerun()
    else:
        st.info("No files imported yet. Upload STEP files to begin.")

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
                    "painting": False,
                    "finishing": None,
                }

        # Load materials and processes
        materials_df = data_loader.get_materials()
        processes_df = data_loader.get_processes()

        # Categorize processes
        cutting_processes = processes_df[processes_df["Category"] == "Cutting"][
            "name"
        ].tolist()
        machining_processes = processes_df[processes_df["Category"] == "Machining"][
            "name"
        ].tolist()
        fabrication_processes = processes_df[processes_df["Category"] == "Fabrication"][
            "name"
        ].tolist()
        finishing_processes = processes_df[processes_df["Category"] == "Finishing"][
            "name"
        ].tolist()

        material_names = materials_df["name"].tolist()

        # Create header row
        header_cols = st.columns([1, 2, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2])
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
        header_cols[11].markdown(
            "<div style='text-align: center'><strong>Painting</strong></div>",
            unsafe_allow_html=True,
        )
        header_cols[12].markdown("**Finishing**")

        st.divider()

        # Create rows for each part
        for idx, file_info in enumerate(st.session_state.uploaded_files):
            part_number = file_info["name"]

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
                    "painting": False,
                    "finishing": None,
                }

            config = st.session_state.part_configs[part_number]

            cols = st.columns([1, 2, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 2])

            with cols[0]:
                st.text("🖼️")  # Placeholder for thumbnail

            with cols[1]:
                st.text(part_number)

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
                st.markdown(
                    "<div style='display: flex; justify-content: center; align-items: center; height: 38px'>",
                    unsafe_allow_html=True,
                )
                painting = st.checkbox(
                    "Painting",
                    value=config["painting"],
                    key=f"paint_{idx}",
                    label_visibility="collapsed",
                )
                st.markdown("</div>", unsafe_allow_html=True)
                config["painting"] = painting

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

with tab3:
    st.header("Costing")
    st.info("Costing calculations will be implemented here.")

with tab4:
    st.header("Export")
    st.info("Export functionality will be implemented here.")
