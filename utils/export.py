import pandas as pd
import io


def generate_csv_export(cost_results, part_name):
    """
    Generates a CSV string from the cost results dictionary. (Imperial Units)
    """
    # Flatten the dictionary
    data = {
        "Part Name": [part_name],
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

    # 1. Collect all unique process names across all parts to create stable columns
    # We want columns like "Process: Laser Cutting ($)"
    # But maybe it's better to just have generic "Cutting", "Machining" columns?
    # The requirement is "includes part config data as well as the costing".

    for item in parts_data:
        p_name = item["name"]
        config = item["config"]
        res = item["result"]

        row = {
            "Part Name": p_name,
            "Quantity": config.get("quantity", 1),
            "Material": config.get("material"),
            "Weight (lbs)": res.get("weight_lbs", 0),
            "Per Part Cost ($)": res.get("per_part_cost", 0),
            "Total Batch Cost ($)": res.get("total_cost_batch", 0),
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

        # Add cost breakdown columns dynamically?
        # Or maybe just sum them up by category?
        # Let's inspect the breakdown list
        # breakdown is a list of dicts like {"Process": "Laser Cutting", "Batch Total Cost": 123.45}

        for entry in res.get("breakdown", []):
            proc_name = entry["Process"]
            cost = entry["Batch Total Cost"]
            # To keep columns manageable, maybe we prefix?
            col_key = f"Cost: {proc_name} ($)"
            row[col_key] = cost

        rows.append(row)

    df = pd.DataFrame(rows)

    # Reorder columns to put standard ones first
    base_cols = [
        "Part Name",
        "Quantity",
        "Material",
        "Weight (lbs)",
        "Per Part Cost ($)",
        "Total Batch Cost ($)",
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
