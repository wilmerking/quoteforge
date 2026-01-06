# QuoteForge Roadmap

This roadmap outlines the development plan for QuoteForge, divided into three strategic phases to move from a functional MVP to a polished, feature-rich production tool.

---

## Phase 1: MVP & Core Foundation

**Goal:** Establish the core analysis engine and basic cost estimation with manual overrides.

- [x] **Infrastructure Setup**
  - Initialize SQLite database schema for materials, manufacturing processes, and labor rates.
  - Setup the Streamlit application framework and project structure.
- [x] **Core Geometry Analysis**
  - Integrate **CadQuery** for robust STEP file parsing.
  - Implement calculation of fundamental properties: Volume, Bounding Box dimensions, and Estimated Mass (depends on material density).
- [x] **Single Part Workflow**
  - Create a simple upload interface for a single STEP file.
  - Display parsed geometry stats in a clean table format.
- [x] **Manual Costing & Basic Logic**
  - Implement a "Manual Override" mode where users can input material price/kg and labor rates.
  - Basic estimation engine: `Cost = (Material Volume * Density * Rate) + (Setup Time * Setup Rate)`.
- [x] **Data Export**
  - Export the single part estimation report to CSV.

---

## Phase 2: Feature Expansion & Automation

**Goal:** Scaling to batch processing, adding visualization, and automating manufacturing intelligence.

- [x] **Batch Processing Capabilities**
  - Support for multi-file STEP uploads.
  - Support for zip file uploads of STEP files.
  - Aggregated view for batch totals (total weight, total cost, material requirements).
- [ ] **Automated Feature Recognition**
  - Implement basic hole detection (count, diameters).
  - Detect sheet metal features (bends) using CadQuery selectors.
  - Automated tapping and drilling cost multipliers based on detected features.
- [ ] **Comprehensive Database Integration**
  - Connect all calculations to the SQLite backend for automated pricing.
  - Add "Complexity Multipliers" to account for difficult geometries.
- [ ] **3D Visualization Utility**
  - Integrate **PyVista** and `stpyvista` for interactive 3D part previews.
  - Highlight detected features (like holes or bends) in the 3D view.
- [ ] **Intelligent Recommendations**
  - Rule-based "Make vs. Buy" logic based on machine capabilities and estimated cost vs. market benchmarks.
- [ ] **Professional Reporting**
  - Generate PDF quotes using ReportLab or similar, including part thumbnails.
- [ ] **Unit Selection**
  - Allow users to select units (metric or imperial) for part specs.

---

## Phase 3: UI/UX Polish & Optimization

**Goal:** Refining the user experience, enhancing visual aesthetics, and performance tuning.

- [ ] **Premium Visual Design**
  - Modernize the Streamlit UI with custom CSS for a premium, professional feel.
  - Refine layout for better information density and visual hierarchy.
- [ ] **Interactive Analytics Dashboards**
  - Add Plotly charts to visualize cost breakdowns (Material vs. Labor vs. Overhead).
  - Batch analytics: compare part costs within a project to identify outliers.
- [ ] **Ease of Use & Presets**
  - Add "Manufacturing Profiles" (e.g., "Prototype Machine Shop", "High-Volume Laser") to quickly switch cost models.
  - Improved file handling with drag-and-drop and folder-level analysis.
- [ ] **Optimization & Robustness**
  - Multi-threaded geometry analysis for large batches.
  - Advanced error handling for corrupted or complex STEP files.
  - Comprehensive logging and user feedback during long-running tasks.
- [ ] **Onboarding & Documentation**
  - Integrated help tooltips and a "Quick Start" guide.
  - Detailed documentation on how cost factors are calculated.
