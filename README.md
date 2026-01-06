# **Quote**Forge

QuoteForge is a professional manufacturing evaluation and quoting tool. It analyzes part geometries from STEP files, calculates detailed cost breakdowns based on materials and manufacturing processes, and generates comprehensive reports.

## 🚀 Key Features

- **4-Step Quoting Workflow**: Streamlined process from file import to final report.
- **Robust Geometry Analysis**: Powered by **CadQuery**, automatically calculates volume, bounding box, and weight.
- **Dynamic Thumbnails**: 2D SVG thumbnails with "Difference" blend mode for perfect visibility on both light and dark system themes.
- **Unit Versatility**: Toggle instantly between **Imperial** and **Metric** units across the entire application and in exported reports.
- **Live Cost Editing**: View detailed breakdowns (Setup vs. Run vs. Material) and manually override any rate or time estimate.
- **Smart Material Selection**: Data-backed material catalog with priority sorting (e.g., Steel A36 at the top).
- **Professional Exports**:
  - **Batch CSV**: Data-dense export optimized for Google Sheets or Excel.
  - **PDF Report**: High-quality branded PDF quotes including part thumbnails and detailed cost tables.
- **Premium UI**: Custom-themed interface with an orange accent (#EA7600) and optimized layout for high information density.

## 🛠️ Tech Stack

- **UI Framework**: Streamlit
- **CAD Engine**: CadQuery (OpenCASCADE)
- **PDF Generation**: ReportLab & Svglib
- **Data Source**: Google Sheets (Synced live for materials and process rates)
- **Language**: Python 3.10+

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.10 or higher
- [Conda](https://docs.conda.io/en/latest/) or Miniconda (Recommended for CadQuery)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/wilmerking/quoteforge.git
   cd quoteforge
   ```

2. The project includes a convenience script `run.sh` that handles dependency installation and starts the application:

   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. Open your browser to the local address displayed (usually `http://localhost:8501`).

## 📖 Usage Guide

1. **Import**: Upload one or more STEP files. You can also load sample files to explore the tool.
2. **Configuration**: Set quantities and manufacturing processes (Cutting, Machining, Finishing, etc.) for each part.
3. **Costing**: Review the estimated costs. You can expand any part to see the line-item breakdown and override specific values.
4. **Export**: Select your units and format (CSV or PDF) and download your final quote.

## 📊 Data Management

QuoteForge uses **Google Sheets** as a live backend for material and process data. This allows manufacturing teams to update pricing and capabilities without touching a single line of code.

- **Syncing**: Data is cached locally to ensure high performance.
- **Customization**: Update the sheet URLs in `data_loader.py` or the configuration files to point to your own manufacturing standards.

---

Built with ❤️ for Modern Manufacturing.
