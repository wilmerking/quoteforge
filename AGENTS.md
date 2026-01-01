# AGENTS.md

Guidelines for AI coding agents working on QuoteForge.

## Project Context

- **Overview**: Streamlit web app for quoting in-house part manufacturing. Upload STEP files (single/batch), analyze geometry with CadQuery, select materials/processes, estimate costs from SQLite DB, recommend in-house vs. outsource.
- **Tech Stack**:
  - Framework: Streamlit (single `app.py` for UI + logic).
  - Geometry: CadQuery (STEP import, volume, mass, basic feature detection).
  - Visualization: PyVista + stpyvista for 3D previews.
  - Database: SQLite (materials, processes, rates).
  - Other: numpy/pandas for calculations, reportlab for PDF export.
- **Key Files**:
  - `app.py`: Main Streamlit app (UI flow, uploads, processing, display).
  - `geometry.py`: CadQuery functions for loading STEP, computing volume/weight/features.
  - `costs.py`: Cost calculation logic and DB interactions.
  - `db/init_db.py`: Setup SQLite with sample data.
  - `utils/`: Helpers (e.g., batch processing, export).

## Coding Guidelines

- Python 3.10+. Follow PEP8, 4-space indent.
- Streamlit best practices: Use `st.cache_data`/`st.cache_resource` for expensive ops (e.g., STEP parsing).
- Modular: Keep geometry, costs, and UI separate.
- Error handling: Graceful for invalid STEP files or batch mismatches.
- Performance: Cache parsed models; approximate complex feature detection initially.
- Testing: pytest for core functions (volume calc, cost formulas).

## Common Tasks for Agents

- Add new process: Extend DB schema + cost formulas; update UI selectbox.
- Improve features: Use CadQuery selectors for better hole/bend detection.
- Batch enhancements: Per-part overrides, zip upload support.
- Export: Implement PDF quotes with tables/charts via ReportLab.
- UI polish: Add progress bars for batch, expandable part details.

Prioritize simplicity and readability. Reference CadQuery docs for geometry, Streamlit docs for UI.

See main README.md for more.
