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
        return (setup_time_mins, hourly_rate)

    return None


def calculate_part_cost(volume_in3, material_info, process_info, manual_overrides=None):
    """
    Calculates cost for a single part using Imperial units.

    volume_in3: Volume in cubic inches
    material_info: (density_lbs_in3, cost_per_lb) or None
    process_info: (setup_time_mins, hourly_rate) or None
    manual_overrides: dict with 'material_cost_per_lb', 'setup_time_mins', 'hourly_rate', 'density_lbs_in3', 'process_time_hours' (optional)
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
    process_time = overrides.get("process_time_hours", 1.0)

    if process_info:
        if setup_time_mins is None:
            setup_time_mins = process_info[0]
        if hourly_rate is None:
            hourly_rate = process_info[1]

    if setup_time_mins is None:
        setup_time_mins = 0.0
    if hourly_rate is None:
        hourly_rate = 0.0

    # Calculate setup cost from time
    setup_cost = (setup_time_mins * hourly_rate) / 60.0

    processing_cost_total = setup_cost + (hourly_rate * process_time)

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
            "used_hourly": hourly_rate,
            "process_time": process_time,
        },
    }
