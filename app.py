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
    st.info("Configuration options will be implemented here.")

with tab3:
    st.header("Costing")
    st.info("Costing calculations will be implemented here.")

with tab4:
    st.header("Export")
    st.info("Export functionality will be implemented here.")
