import pandas as pd
import os
import tempfile
import io
from reportlab.lib import colors  # type: ignore
from reportlab.lib.pagesizes import letter  # type: ignore
from reportlab.lib.styles import getSampleStyleSheet  # type: ignore
from reportlab.platypus import (  # type: ignore
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from svglib.svglib import svg2rlg  # type: ignore


def generate_csv_export(cost_results, part_name):
    """
    Generates a CSV string from the cost results dictionary. (Imperial Units)
    """
    # Flatten the dictionary
    data = {
        "Part Name": [cost_results.get("display_name", part_name)],
        "Material Cost ($)": [cost_results["material_cost"]],
        "Processing Cost ($)": [cost_results["processing_cost"]],
        "Total Cost ($)": [cost_results["total_cost"]],
        "Mass (lbs)": [cost_results["details"].get("mass_lbs", 0)],
        "Used Density (lbs/in³)": [cost_results["details"].get("used_density", 0)],
        "Used Material Rate ($/lb)": [
            cost_results["details"].get("used_material_rate", 0)
        ],
        "Setup Cost ($)": [cost_results["details"].get("used_setup", 0)],
        "Hourly Rate ($/hr)": [cost_results["details"].get("used_hourly", 0)],
        "Process Time (hr)": [cost_results["details"].get("process_time", 0)],
    }

    df = pd.DataFrame(data)
    return df.to_csv(index=False)


def generate_batch_export(parts_data):
    """
    Generates a CSV string for a batch of parts.

    Args:
        parts_data: List of dicts, each containing:
            - name: Part Name
            - config: Configuration dict
            - result: Result from costs.calculate_part_breakdown

    Returns:
        CSV string
    """
    rows = []

    for item in parts_data:
        p_file_name = item["name"]
        # Use display name (no file extension)
        p_name = os.path.splitext(p_file_name)[0].replace("_", "-")
        config = item["config"]
        res = item["result"]

        material_cost_total = 0.0

        row = {
            "Part Name": p_name,
            "Quantity": config.get("quantity", 1),
            "Material": config.get("material"),
            "Weight (lbs)": res.get("weight_lbs", 0),
            "Per Part Cost ($)": res.get("per_part_cost", 0),
            "Total Cost ($)": res.get("total_cost_batch", 0),
            # Config Columns
            "Cutting": config.get("cutting", "None"),
            "Machining": config.get("machining", False),
            "Turning": config.get("turning", False),
            "3D Printing": config.get("3d_printing", False),
            "Forming": config.get("forming", False),
            "Threading": config.get("threading", False),
            "Welding": config.get("welding", False),
            "Finishing": config.get("finishing", "None"),
        }

        # Consolidate material costs and add other process costs
        for entry in res.get("breakdown", []):
            proc_name = entry["Process"]
            cost = entry["Batch Total Cost"]
            if proc_name.startswith("Material:"):
                material_cost_total += cost
            else:
                col_key = f"Cost: {proc_name} ($)"
                row[col_key] = cost

        row["Material Cost (#)"] = material_cost_total

        rows.append(row)

    df = pd.DataFrame(rows)

    # Reorder columns to put standard ones first
    base_cols = [
        "Part Name",
        "Quantity",
        "Material",
        "Weight (lbs)",
        "Material Cost (#)",
        "Per Part Cost ($)",
        "Total Cost ($)",
        "Cutting",
        "Machining",
        "Turning",
        "3D Printing",
        "Forming",
        "Threading",
        "Welding",
        "Finishing",
    ]

    # Identify dynamic cost columns
    existing_cols = list(df.columns)
    cost_cols = [c for c in existing_cols if c not in base_cols]
    cost_cols.sort()  # Alphabetical sort for cost columns

    final_cols = base_cols + cost_cols
    # Ensure all base_cols exist (in case of empty data)
    for c in base_cols:
        if c not in df.columns:
            df[c] = None

    df = df[final_cols]

    return df.to_csv(index=False)


def generate_pdf_export(parts_data):
    """
    Generates a PDF report for a batch of parts.

    Args:
        parts_data: List of dicts, same as generate_batch_export but may include 'thumbnail_svg'

    Returns:
        bytes: The PDF file content
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    story = []
    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    h2_style = styles["Heading2"]
    h2_style.spaceAfter = 5
    h2_style.spaceBefore = 10

    h3_style = styles["Heading3"]
    h3_style.spaceAfter = 2
    h3_style.spaceBefore = 5

    normal_style = styles["Normal"]

    # Report Title
    story.append(Paragraph("QuoteForge Part Report", title_style))
    story.append(Spacer(1, 10))

    for item in parts_data:
        p_file_name = item["name"]
        p_name = os.path.splitext(p_file_name)[0].replace("_", "-")
        config = item["config"]
        res = item["result"]
        svg_content = item.get("thumbnail_svg")

        # Part Header
        story.append(Paragraph(f"Part: {p_name}", h2_style))
        story.append(Spacer(1, 2))

        # --- Top Section: Thumbnail + Specs ---

        # 1. Prepare Thumbnail
        drawing = None
        if svg_content:
            try:
                # Ensure the thumbnail is visible on white PDF background by changing white stroke to black
                svg_content = svg_content.replace(
                    'stroke="rgb(255,255,255)"', 'stroke="rgb(0,0,0)"'
                )
                svg_content = svg_content.replace(
                    'stroke="#ffffff"', 'stroke="#000000"'
                )
                svg_content = svg_content.replace(
                    'stroke="#FFFFFF"', 'stroke="#000000"'
                )

                # svglib needs a file path
                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".svg", mode="w"
                ) as tmp_svg:
                    tmp_svg.write(svg_content)
                    tmp_svg_path = tmp_svg.name

                drawing = svg2rlg(tmp_svg_path)
                os.remove(tmp_svg_path)

                if drawing:
                    # Resize drawing to fit nicely (e.g., width 200)
                    desired_width = 200
                    scale_factor = desired_width / drawing.width
                    drawing.width *= scale_factor
                    drawing.height *= scale_factor
                    drawing.scale(scale_factor, scale_factor)
            except Exception as e:
                print(f"Error processing SVG for {p_name}: {e}")
                drawing = None

        # 2. Prepare Specs Table
        # Data for specs
        specs_data = [
            ["Quantity:", str(config.get("quantity", 1))],
            ["Material:", str(config.get("material", "-"))],
            ["Weight:", f"{res.get('weight_lbs', 0):.2f} lbs"],
            ["Per Part Cost:", f"${res.get('per_part_cost', 0):.2f}"],
            ["Total Cost:", f"${res.get('total_cost_batch', 0):.2f}"],
        ]

        specs_table = Table(specs_data, colWidths=[100, 150])
        specs_table.setStyle(
            TableStyle(
                [
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
                ]
            )
        )

        # Layout for Top Section
        # If we have a drawing, use a 2-column layout. If not, just specs.
        if drawing:
            # We can't put a Drawing directly into a Table cell easily with Flowables?
            # Actually we can if we wrap it in renderPDF.GraphicsFlowable or similar?
            # svglib returns a Drawing, which is a Flowable.

            # Create a table with 2 columns: [Drawing, SpecsTable]
            top_data = [[drawing, specs_table]]
            top_layout = Table(top_data, colWidths=[250, 260])
            top_layout.setStyle(
                TableStyle(
                    [
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("ALIGN", (0, 0), (0, 0), "CENTER"),  # Center image
                    ]
                )
            )
            story.append(top_layout)
        else:
            story.append(specs_table)

        story.append(Spacer(1, 5))

        # --- Bottom Section: Cost Breakdown ---
        story.append(Paragraph("Cost Breakdown", h3_style))
        # (Spacer removed as style has spaceBefore/spaceAfter)

        breakdown_list = res.get("breakdown", [])
        if breakdown_list:
            # Table Header
            table_data = [
                [
                    "Process",
                    "Rate",
                    "Setup (mins)",
                    "Run (mins)",
                    "Setup $",
                    "Run $",
                    "Batch Total $",
                ]
            ]

            for row in breakdown_list:
                table_data.append(
                    [
                        row.get("Process", ""),
                        f"{row.get('Rate', 0):.2f}",
                        f"{row.get('Setup Mins', 0):.1f}"
                        if row.get("Setup Mins") is not None
                        else "-",
                        f"{row.get('Run Mins', 0):.1f}"
                        if row.get("Run Mins") is not None
                        else "-",
                        f"${row.get('Setup Cost', 0):.2f}"
                        if row.get("Setup Cost") is not None
                        else "-",
                        f"${row.get('Run Cost', 0):.2f}"
                        if row.get("Run Cost") is not None
                        else "-",
                        f"${row.get('Batch Total Cost', 0):.2f}",
                    ]
                )

            bd_table = Table(table_data, colWidths=[140, 50, 60, 60, 60, 60, 80])
            bd_table.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f0f2f6")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                        ("ALIGN", (0, 0), (0, -1), "LEFT"),  # Process column left align
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTSIZE", (0, 0), (-1, -1), 9),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ]
                )
            )
            story.append(bd_table)
        else:
            story.append(Paragraph("No cost details available.", normal_style))

        story.append(Spacer(1, 30))
        # Add a visual divider
        story.append(Paragraph("_" * 60, normal_style))
        story.append(Spacer(1, 30))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
