"""
Cost calculation module for QuoteForge.
Updated to use Google Sheets data via data_loader instead of SQLite.
"""

import data_loader


def get_material_rate(material_name):
    """
    Fetches (density_lbs_in3, cost_per_lb) for a given material name.

    Returns:
        Tuple of (density, cost_per_lb) or None if not found
    """
    material = data_loader.get_material_by_name(material_name)

    if material is not None:
        # Access DataFrame columns by name
        density = material["density (lb/in^3)"]
        cost_per_lb = material["cost_per_lb"]
        return (density, cost_per_lb)

    return None


def get_process_rates(process_name):
    """
    Fetches (setup_time_mins, hourly_rate) for a given process name.

    Returns:
        Tuple of (setup_time_mins, hourly_rate) or None if not found
    """
    process = data_loader.get_process_by_name(process_name)

    if process is not None:
        setup_time_mins = process["setup_time_mins"]
        hourly_rate = process["hourly_rate"]
        run_time_mins = process.get("run_time_mins", 60.0)  # Default to 60 if missing
        return (setup_time_mins, hourly_rate, run_time_mins)

    return None


def calculate_part_cost(volume_in3, material_info, process_info, manual_overrides=None):
    """
    Calculates cost for a single part using Imperial units.

    volume_in3: Volume in cubic inches
    material_info: (density_lbs_in3, cost_per_lb) or None
    process_info: (setup_time_mins, hourly_rate) or None
    manual_overrides: dict with 'material_cost_per_lb', 'setup_time_mins', 'hourly_rate', 'density_lbs_in3', 'run_time_mins' (optional)
    """

    overrides = manual_overrides or {}

    # Material Cost
    density = overrides.get("density_lbs_in3")
    cost_per_lb = overrides.get("material_cost_per_lb")

    if material_info:
        if density is None:
            density = material_info[0]
        if cost_per_lb is None:
            cost_per_lb = material_info[1]

    if density is None or cost_per_lb is None:
        material_cost_total = 0.0
        mass_lbs = 0.0
    else:
        # volume is in3, density lbs/in3 -> mass in lbs
        mass_lbs = volume_in3 * density
        material_cost_total = mass_lbs * cost_per_lb

    # Process Cost
    setup_time_mins = overrides.get("setup_time_mins")
    hourly_rate = overrides.get("hourly_rate")
    run_time_mins = overrides.get("run_time_mins", 60.0)

    if process_info:
        if setup_time_mins is None:
            setup_time_mins = process_info[0]
        if hourly_rate is None:
            hourly_rate = process_info[1]

    if setup_time_mins is None:
        setup_time_mins = 0.0
    if hourly_rate is None:
        hourly_rate = 0.0

    # Calculate costs from time
    setup_cost = (setup_time_mins * hourly_rate) / 60.0
    run_cost = (run_time_mins * hourly_rate) / 60.0

    processing_cost_total = setup_cost + run_cost

    total_cost = material_cost_total + processing_cost_total

    return {
        "material_cost": round(material_cost_total, 2),
        "processing_cost": round(processing_cost_total, 2),
        "total_cost": round(total_cost, 2),
        "details": {
            "mass_lbs": round(mass_lbs, 3),
            "used_density": density,
            "used_material_rate": cost_per_lb,
            "used_setup_mins": setup_time_mins,
            "used_setup_cost": round(setup_cost, 2),
            "used_run_mins": run_time_mins,
            "used_run_cost": round(run_cost, 2),
            "used_hourly": hourly_rate,
        },
    }


def calculate_part_breakdown(config, volume_in3, overrides=None):
    """
    Calculates detailed cost breakdown for a part based on its configuration.

    Args:
        config: Dict containing part configuration (qty, material, processes)
        volume_in3: Volume in cubic inches
        overrides: Dict of manual cost overrides

    Returns:
        Dict containing full cost breakdown, batch totals, and flat fields for export
    """
    overrides = overrides or {}
    quantity = config.get("quantity", 1)
    material_name = config.get("material")

    # 1. Material Cost
    weight_lbs = 0.0
    material_cost_per_lb = 0.0
    material_cost_batch = 0.0
    density = 0.0

    if material_name:
        mat_info = get_material_rate(material_name)
        if mat_info:
            density = mat_info[0]
            material_cost_per_lb = mat_info[1]
            weight_lbs = volume_in3 * density

    # Material Overrides
    mat_key = f"Material: {material_name}"
    mat_ovr = overrides.get(mat_key, {})
    eff_mat_rate = float(mat_ovr.get("rate", material_cost_per_lb))

    cost_details = []

    if material_name and weight_lbs > 0:
        material_cost_single = weight_lbs * eff_mat_rate
        material_cost_batch = material_cost_single * quantity

        cost_details.append(
            {
                "Process": mat_key,
                "Rate": eff_mat_rate,
                "Unit": "$/lbs",
                "Setup Mins": None,
                "Run Mins": None,
                "Setup Cost": None,
                "Run Cost": None,
                "Batch Total Cost": material_cost_batch,
            }
        )

    # 2. Process Costs
    batch_total_process_cost = 0.0

    # helper to process a single process step
    def process_step(p_name):
        nonlocal batch_total_process_cost

        # Get base rates
        p_info = get_process_rates(p_name)
        # Returns (setup_mins, hourly_rate, run_mins_default)
        if not p_info:
            return

        # Check overrides
        p_ovr = overrides.get(p_name, {})

        setup_mins = float(p_ovr.get("setup_time_mins", p_info[0]))
        rate = float(p_ovr.get("rate", p_info[1]))
        run_mins = float(p_ovr.get("run_time_mins", p_info[2]))

        setup_cost = (setup_mins * rate) / 60.0
        run_cost_single = (run_mins * rate) / 60.0
        run_cost_batch = run_cost_single * quantity

        batch_cost = setup_cost + run_cost_batch

        batch_total_process_cost += batch_cost

        cost_details.append(
            {
                "Process": p_name,
                "Rate": rate,
                "Unit": "$/hr",
                "Setup Mins": setup_mins,
                "Run Mins": run_mins,
                "Setup Cost": setup_cost,
                "Run Cost": run_cost_single,
                "Batch Total Cost": batch_cost,  # This is the total for the whole batch including ONE setup
            }
        )

    # Cutting
    if config.get("cutting"):
        process_step(config["cutting"])

    # Boolean Processes
    bool_processes = [
        "Machining",
        "Turning",
        "3D Printing",
        "Forming",
        "Threading",
        "Welding",
    ]
    # Map config keys to process names
    config_map = {
        "machining": "Machining",
        "turning": "Turning",
        "3d_printing": "3D Printing",
        "forming": "Forming",
        "threading": "Threading",
        "welding": "Welding",
    }

    for key, p_name in config_map.items():
        if config.get(key, False):
            process_step(p_name)

    # Finishing
    if config.get("finishing"):
        process_step(config["finishing"])

    total_cost_batch = material_cost_batch + batch_total_process_cost
    per_part_cost = total_cost_batch / quantity if quantity > 0 else 0.0

    return {
        "weight_lbs": weight_lbs,
        "quantity": quantity,
        "per_part_cost": per_part_cost,
        "total_cost_batch": total_cost_batch,
        "breakdown": cost_details,
    }
