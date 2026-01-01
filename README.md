# QuoteForge

QuoteForge is a web application designed to evaluate parts for in-house manufacturing and generate quotes. It analyzes part geometries from STEP files, estimates costs based on materials, processes, and features, and provides recommendations on whether to manufacture in-house or outsource prototyping/production. Supports batch processing for multiple parts.

## Overview

This tool helps manufacturing teams quickly assess the feasibility and cost of producing parts internally. By importing 3D models (single or batch), selecting materials and processes, and leveraging a simple cost database, QuoteForge delivers accurate estimates and smart recommendations.

Built entirely in Python with **Streamlit** for the interactive web UI and **CadQuery** for STEP file parsing and geometry analysis (volume, weight, basic features).

## Features

- **Part Import**: Upload one or multiple STEP files (batch processing).
- **Material Selection**: Choose from predefined materials with costs and densities.
- **Process Selection**: Support for processes like machining, laser cutting, forming, tapping.
- **Geometry Analysis**: Automatically compute volume, bounding box, estimated weight, and basic feature detection (e.g., holes, bends via approximations).
- **Batch Processing**: Analyze multiple parts at once, with per-part details and aggregated totals.
- **Material Database**: Lightweight SQLite for material options, costs, and densities.
- **Cost Database**: Lightweight SQLite for process costs, setup times, per-part rates, and complexity multipliers.
- **Estimations**: Detailed cost breakdowns (material + process + setup) per part and batch.
- **Recommendations**: Simple rule-based suggestion (in-house if below threshold, else outsource).
- **Visualization**: Interactive 3D preview of parts using PyVista in Streamlit.

## Installation

1. Clone the repository:

   `git clone https://github.com/wilmerking/quoteforge.git`

2. Navigate to the project directory:

   `cd quoteforge`

3. Create a virtual environment and install dependencies:

   `python -m venv venv`
   `source venv/bin/activate`
   `pip install -r requirements.txt`

4. Initialize the database (pre-populate with sample materials/processes):

   `python db/init_db.py`

5. Run the app:

   `streamlit run app.py`

6. Open your browser (default: http://localhost:8501).

7. Upload STEP file(s) – single or multiple for batch.

8. Select material and processes (global for batch, or per-part if varying).

9. View 3D previews, geometry stats, cost estimates, and recommendations.

10. Export results as CSV or PDF summary.

## Tech Stack Details

- **UI**: Streamlit (fast prototyping, file upload, tables, charts).
- **Geometry**: CadQuery (excellent STEP import, volume/mass properties, selectors for features).
- **3D Preview**: PyVista + stpyvista component for interactive rendering in Streamlit.
- **Database**: SQLite (simple, file-based).
- **Future Extensions**: Add ReportLab for PDF quotes, more advanced feature recognition.
