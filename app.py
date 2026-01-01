import streamlit as st
import os
import tempfile
import sqlite3
import geometry
import costs
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
tab1, tab2 = st.tabs(["Single Part", "Batch Processing"])

with tab1:
    st.header("Single Part Estimation")
    uploaded_file = st.file_uploader("Upload STEP File", type=["stp", "step"])

    if uploaded_file:
        # Save uploaded file to temp
        with tempfile.NamedTemporaryFile(delete=False, suffix=".step") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name

        st.success(f"File uploaded: {uploaded_file.name}")

        # Geometry Analysis
        try:
            with st.spinner("Analyzing geometry..."):
                analyzer = geometry.GeometryAnalyzer(tmp_path)
                volume = analyzer.get_volume()
                bbox = analyzer.get_bounding_box()

            st.subheader("Geometry Analysis")
            col1, col2, col3 = st.columns(3)
            col1.metric("Volume (in³)", f"{volume:.2f}")
            col2.metric(
                "Bounding Box (in)", f"{bbox[0]:.2f} x {bbox[1]:.2f} x {bbox[2]:.2f}"
            )

            # Costing Inputs
            st.subheader("Cost Estimation")

            conn = sqlite3.connect("quoteforge.db")  # Direct connection for dropdowns
            cursor = conn.cursor()

            # Material Selection
            cursor.execute("SELECT name FROM materials")
            materials = [r[0] for r in cursor.fetchall()]
            selected_material = st.selectbox("Select Material", materials)

            # Process Selection
            cursor.execute("SELECT name FROM processes")
            processes = [r[0] for r in cursor.fetchall()]
            selected_process = st.selectbox("Select Process", processes)
            conn.close()

            # Manual Overrides
            with st.expander("Manual Overrides"):
                m_density = st.number_input(
                    "Override Density (lbs/in³)", value=0.0, format="%.4f"
                )
                m_cost = st.number_input("Override Material Cost ($/lb)", value=0.0)
                m_setup = st.number_input("Override Setup Cost ($)", value=0.0)
                m_rate = st.number_input("Override Hourly Rate ($/hr)", value=0.0)
                process_time = st.number_input("Process Time (hours)", value=1.0)

            # Perform Calculation
            mat_info = costs.get_material_rate(selected_material)
            proc_info = costs.get_process_rates(selected_process)

            overrides = {}
            if m_density > 0:
                overrides["density_lbs_in3"] = m_density
            if m_cost > 0:
                overrides["material_cost_per_lb"] = m_cost
            if m_setup > 0:
                overrides["setup_cost"] = m_setup
            if m_rate > 0:
                overrides["hourly_rate"] = m_rate
            overrides["process_time_hours"] = process_time

            cost_res = costs.calculate_part_cost(volume, mat_info, proc_info, overrides)

            st.divider()
            st.metric("Estimated Mass", f"{cost_res['details']['mass_lbs']:.3f} lbs")

            c1, c2, c3 = st.columns(3)
            c1.metric("Material Cost", f"${cost_res['material_cost']}")
            c2.metric("Processing Cost", f"${cost_res['processing_cost']}")
            c3.metric("Total Cost", f"${cost_res['total_cost']}")

            # Export
            st.divider()
            csv_data = export.generate_csv_export(cost_res, uploaded_file.name)
            st.download_button(
                label="Download Estimate CSV",
                data=csv_data,
                file_name=f"estimate_{uploaded_file.name}.csv",
                mime="text/csv",
            )

            # Cleanup
            os.remove(tmp_path)

        except Exception as e:
            st.error(f"Error analyzing file: {e}")

with tab2:
    st.header("Batch Processing")
    st.info("Batch processing coming in Phase 2.")
