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
