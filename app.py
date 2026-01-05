import streamlit as st  # type: ignore
import os
import tempfile
import glob
import geometry
import costs
import data_loader
import pandas as pd  # type: ignore
from utils import export

print("DEBUG: Geometry imported successfully")
print("DEBUG: Costs imported successfully")
print("DEBUG: Export imported successfully")

st.set_page_config(page_title="QuoteForge", layout="wide")
st.markdown(
    """
    <style>
    /* Cap the width of number inputs so they don't stretch unnecessarily */
    div[data-testid="stNumberInput"] {
        max-width: 150px;
    }
    /* Match number input labels to metric labels for consistency */
    div[data-testid="stNumberInput"] label p {
        font-size: 0.8rem !important;
        color: rgba(250, 250, 250, 0.6) !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

if "cost_overrides" not in st.session_state:
    st.session_state.cost_overrides = {}


def update_cost_overrides(part_number, key, df_ref):
    """
    Callback to update cost overrides based on data_editor changes.
    df_ref is the DataFrame used to populate the editor, used to lookup Process names.
    """
    if key not in st.session_state:
        return

    changes = st.session_state[key].get("edited_rows", {})
    if not changes:
        return

    if part_number not in st.session_state.cost_overrides:
        st.session_state.cost_overrides[part_number] = {}

    for idx, row_changes in changes.items():
        # Get the process name from the reference DataFrame (by index)
        # We use iloc[idx] because edited_rows keys are 0-based indices matching the data
        process_name_full = df_ref.iloc[idx]["Process"]

        # If it's a material row, it might look like "Material: Aluminum 6061"
        # We'll store it by the full string key for simplicity in lookup
        process_key = process_name_full

        if process_key not in st.session_state.cost_overrides[part_number]:
            st.session_state.cost_overrides[part_number][process_key] = {}

        # Map column names to internal override keys
        # We expect columns: "Rate", "Setup Mins", "Run Mins"
        col_map = {
            "Rate": "rate",
            "Setup Mins": "setup_time_mins",
            "Run Mins": "run_time_mins",
        }

        for col_name, new_val in row_changes.items():
            if col_name in col_map:
                override_key = col_map[col_name]
                st.session_state.cost_overrides[part_number][process_key][
                    override_key
                ] = new_val


def update_quantity(part_number, key, other_key):
    """
    Callback to sync quantity across different tabs and update part_configs.
    """
    if key in st.session_state:
        new_qty = st.session_state[key]
        st.session_state.part_configs[part_number]["quantity"] = new_qty
        if other_key:
            st.session_state[other_key] = new_qty


st.title("QuoteForge")

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

    st.divider()
    col_btn1, col_btn2, _ = st.columns([0.15, 0.15, 0.7])
    with col_btn1:
        if st.button("Load Sample Files", use_container_width=True):
            samples_dir = os.path.join(os.getcwd(), "samples")
            if os.path.exists(samples_dir):
                sample_files = glob.glob(
                    os.path.join(samples_dir, "*.step")
                ) + glob.glob(os.path.join(samples_dir, "*.stp"))

                added_count = 0
                for sample_path in sample_files:
                    file_name = os.path.basename(sample_path)
                    existing_names = [
                        f["name"] for f in st.session_state.uploaded_files
                    ]
                    if file_name not in existing_names:
                        # Copy to temp file to maintain consistency with uploader
                        with tempfile.NamedTemporaryFile(
                            delete=False, suffix=".step"
                        ) as tmp:
                            with open(sample_path, "rb") as sf:
                                tmp.write(sf.read())
                            tmp_path = tmp.name

                        st.session_state.uploaded_files.append(
                            {
                                "name": file_name,
                                "path": tmp_path,
                                "size": os.path.getsize(sample_path),
                            }
                        )
                        added_count += 1

                if added_count > 0:
                    st.success(f"Added {added_count} sample file(s)")
                    st.rerun()
                else:
                    st.info("Sample files already loaded.")
            else:
                st.error("Samples directory not found.")

    with col_btn2:
        if st.button("Clear All Files", use_container_width=True, type="secondary"):
            st.session_state.uploaded_files = []
            st.session_state.part_configs = {}
            st.session_state.cost_overrides = {}
            # Also clear cached geometry/thumbnails keys from session state if present
            keys_to_clear = [
                k
                for k in st.session_state.keys()
                if k.startswith("thumb_")
                or k.startswith("vol_")
                or k.startswith("qty_")
                or k.startswith("cost_qty_")
            ]
            for k in keys_to_clear:
                del st.session_state[k]
            st.rerun()


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
            [100, 100, 100, 150, 100, 80, 80, 80, 80, 80, 80, 100],
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
                [100, 100, 100, 150, 100, 80, 80, 80, 80, 80, 80, 100],
                vertical_alignment="center",
            )

            with cols[0]:
                # Generate thumbnail and geometry info
                file_path = file_info["path"]
                thumb_key = f"thumb_v2_{part_number}"

                # We store result in session state to avoid re-analyzing on every widget interaction
                # Note: geometry analyzer is still needed for volume calculation in tab 3, but we can do it here too
                if thumb_key not in st.session_state:
                    try:
                        analyzer = geometry.GeometryAnalyzer(file_path)
                        svg_data = analyzer.get_thumbnail_svg()
                        if svg_data:
                            st.session_state[thumb_key] = svg_data
                        # Also cache volume if we already have the analyzer
                        st.session_state[f"vol_{part_number}"] = analyzer.get_volume()
                    except Exception as e:
                        st.error(f"Failed to generate thumbnail: {e}")
                        pass

                if thumb_key in st.session_state:
                    import base64

                    svg_data = st.session_state[thumb_key]
                    b64_svg = base64.b64encode(svg_data.encode("utf-8")).decode("utf-8")
                    st.markdown(
                        f'<img src="data:image/svg+xml;base64,{b64_svg}" style="max-width: 100%; height: auto;"/>',
                        unsafe_allow_html=True,
                    )
                else:
                    st.text("🖼️")

            with cols[1]:
                st.text(display_name)

            with cols[2]:
                st.number_input(
                    "Qty",
                    min_value=1,
                    value=int(config["quantity"]),
                    key=f"qty_{part_number}",
                    label_visibility="collapsed",
                    on_change=update_quantity,
                    args=(part_number, f"qty_{part_number}", f"cost_qty_{part_number}"),
                )

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
                machining = st.checkbox(
                    "Machining",
                    value=config["machining"],
                    key=f"mach_{idx}",
                    label_visibility="collapsed",
                )
                config["machining"] = machining

            with cols[6]:
                turning = st.checkbox(
                    "Turning",
                    value=config["turning"],
                    key=f"turn_{idx}",
                    label_visibility="collapsed",
                )
                config["turning"] = turning

            with cols[7]:
                printing_3d = st.checkbox(
                    "3D Printing",
                    value=config["3d_printing"],
                    key=f"3dprint_{idx}",
                    label_visibility="collapsed",
                )
                config["3d_printing"] = printing_3d

            with cols[8]:
                forming = st.checkbox(
                    "Forming",
                    value=config["forming"],
                    key=f"form_{idx}",
                    label_visibility="collapsed",
                )
                config["forming"] = forming

            with cols[9]:
                threading = st.checkbox(
                    "Threading",
                    value=config["threading"],
                    key=f"thread_{idx}",
                    label_visibility="collapsed",
                )
                config["threading"] = threading

            with cols[10]:
                welding = st.checkbox(
                    "Welding",
                    value=config["welding"],
                    key=f"weld_{idx}",
                    label_visibility="collapsed",
                )
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

            # Get geometry info from session state or analyzer
            vol_key = f"vol_{part_number}"
            if vol_key in st.session_state:
                volume_in3 = st.session_state[vol_key]
            else:
                try:
                    analyzer = geometry.GeometryAnalyzer(file_path)
                    volume_in3 = analyzer.get_volume()
                    st.session_state[vol_key] = volume_in3
                except Exception as e:
                    volume_in3 = 0.0
                    st.error(f"Error analyzing {part_number}: {e}")

            # Get manual overrides
            overrides = st.session_state.cost_overrides.get(part_number, {})

            # Calculate detailed costs
            cost_result = costs.calculate_part_breakdown(config, volume_in3, overrides)

            weight_lbs = cost_result["weight_lbs"]
            per_part_cost = cost_result["per_part_cost"]
            total_cost = cost_result["total_cost_batch"]
            grand_total += total_cost

            cost_details = cost_result["breakdown"]

            # Render Card
            with st.container(border=True):
                col_img, col_info, col_toggle = st.columns(
                    [1, 4, 0.1]
                )  # Adjusted for simple expander later

                with col_img:
                    thumb_key = f"thumb_v2_{part_number}"
                    if thumb_key in st.session_state:
                        svg_data = st.session_state[thumb_key]
                        import base64

                        b64_svg = base64.b64encode(svg_data.encode("utf-8")).decode(
                            "utf-8"
                        )
                        st.markdown(
                            f'<img src="data:image/svg+xml;base64,{b64_svg}" style="max-width: 100%; height: auto;"/>',
                            unsafe_allow_html=True,
                        )
                    else:
                        st.text("🖼️")  # Fallback
                        st.caption("No Thumbnail")

                with col_info:
                    st.subheader(display_name)

                    metric_cols = st.columns([1, 0.6, 1.2, 1.2])
                    metric_cols[0].metric("Weight", f"{weight_lbs:.2f} lbs")
                    metric_cols[1].number_input(
                        "Quantity",
                        min_value=1,
                        value=int(quantity),
                        key=f"cost_qty_{part_number}",
                        on_change=update_quantity,
                        args=(
                            part_number,
                            f"cost_qty_{part_number}",
                            f"qty_{part_number}",
                        ),
                    )
                    metric_cols[2].metric("Per Part Cost", f"${per_part_cost:.2f}")
                    metric_cols[3].metric("Total Cost", f"${total_cost:.2f}")

                # Details Expander
                with st.expander("Cost Breakdown"):
                    if cost_details:
                        df = pd.DataFrame(cost_details)
                        st.data_editor(
                            df,
                            key=f"editor_{part_number}",
                            use_container_width=True,
                            hide_index=True,
                            num_rows="fixed",
                            disabled=[
                                "Process",
                                "Unit",
                                "Setup Cost",
                                "Run Cost",
                                "Batch Total Cost",
                            ],
                            column_config={
                                "Rate": st.column_config.NumberColumn(
                                    "Rate", format="%.2f", min_value=0.0
                                ),
                                "Setup Mins": st.column_config.NumberColumn(
                                    "Setup (mins)", format="%.1f", min_value=0.0
                                ),
                                "Run Mins": st.column_config.NumberColumn(
                                    "Run (mins)", format="%.1f", min_value=0.0
                                ),
                                "Setup Cost": st.column_config.NumberColumn(
                                    "Setup Cost", format="$%.2f"
                                ),
                                "Run Cost": st.column_config.NumberColumn(
                                    "Run Cost", format="$%.2f"
                                ),
                                "Batch Total Cost": st.column_config.NumberColumn(
                                    "Batch Total Cost", format="$%.2f"
                                ),
                            },
                            on_change=update_cost_overrides,
                            args=(part_number, f"editor_{part_number}", df),
                        )

                        # Reset Defaults button
                        has_overrides = (
                            part_number in st.session_state.cost_overrides
                            and bool(st.session_state.cost_overrides[part_number])
                        )
                        if st.button(
                            "Reset to Defaults",
                            key=f"reset_{part_number}",
                            disabled=not has_overrides,
                        ):
                            if part_number in st.session_state.cost_overrides:
                                del st.session_state.cost_overrides[part_number]
                            # Clear the editor's internal state to ensure it resets visually
                            if f"editor_{part_number}" in st.session_state:
                                del st.session_state[f"editor_{part_number}"]
                            st.rerun()
                    else:
                        st.info("No costs associated.")
        # Grand total
        st.markdown(f"### Grand Total: **${grand_total:.2f}**")

with tab4:
    st.header("Export")

    if not st.session_state.uploaded_files:
        st.warning("No files imported.")
    else:
        st.write(
            "Download a detailed CSV containing configuration and cost breakdown for all imported parts."
        )

        # Prepare data for export
        export_data = []

        # We need to re-calculate costs (or cache them?)
        # For safety and latest state, we re-calculate using the shared function
        for file_info in st.session_state.uploaded_files:
            part_number = file_info["name"]
            file_path = file_info["path"]

            # 1. Config
            config = st.session_state.part_configs.get(part_number, {})

            # 2. Volume (Reuse session state if available, else re-analyze - though Tab 3 logic likely populated it)
            vol_key = f"vol_{part_number}"
            volume_in3 = st.session_state.get(vol_key, 0.0)
            if volume_in3 == 0.0:
                try:
                    analyzer = geometry.GeometryAnalyzer(file_path)
                    volume_in3 = analyzer.get_volume()
                except:  # noqa: E722
                    pass

            # 3. Overrides
            overrides = st.session_state.cost_overrides.get(part_number, {})

            # Calculate
            result = costs.calculate_part_breakdown(config, volume_in3, overrides)

            export_data.append(
                {"name": part_number, "config": config, "result": result}
            )

        # Generate CSV
        if export_data:
            csv_data = export.generate_batch_export(export_data)

            st.download_button(
                label="Download Batch CSV",
                data=csv_data,
                file_name="quoteforge_batch_export.csv",
                mime="text/csv",
            )
