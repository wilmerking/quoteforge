import sqlite3
import os

DB_PATH = "quoteforge.db"


def get_material_rate(material_name):
    """Fetches (density, cost_per_kg) for a given material name."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT density, cost_per_kg FROM materials WHERE name = ?", (material_name,)
    )
    result = cursor.fetchone()
    conn.close()
    if result:
        return result  # (density, cost_per_kg)
    return None


def get_process_rates(process_name):
    """Fetches (setup_cost, hourly_rate) for a given process name."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT setup_cost, hourly_rate FROM processes WHERE name = ?", (process_name,)
    )
    result = cursor.fetchone()
    conn.close()
    if result:
        return result  # (setup_cost, hourly_rate)
    return None


def calculate_part_cost(volume_cm3, material_info, process_info, manual_overrides=None):
    """
    Calculates cost for a single part.
    material_info: (density_g_cm3, cost_per_kg) or None
    process_info: (setup_cost, hourly_rate) or None
    manual_overrides: dict with 'material_cost_per_kg', 'setup_cost', 'hourly_rate', 'density', 'process_time_hours' (optional)
    """

    overrides = manual_overrides or {}

    # Material Cost
    density = overrides.get("density")
    cost_per_kg = overrides.get("material_cost_per_kg")

    if material_info:
        if density is None:
            density = material_info[0]
        if cost_per_kg is None:
            cost_per_kg = material_info[1]

    if density is None or cost_per_kg is None:
        material_cost_total = 0.0  # Cannot calculate
    else:
        # volume is cm3, density g/cm3 -> mass in grams
        mass_g = volume_cm3 * density
        mass_kg = mass_g / 1000.0
        material_cost_total = mass_kg * cost_per_kg

    # Process Cost
    setup_cost = overrides.get("setup_cost")
    hourly_rate = overrides.get("hourly_rate")
    process_time = overrides.get(
        "process_time_hours", 1.0
    )  # Default 1 hour if not specified/calculated

    if process_info:
        if setup_cost is None:
            setup_cost = process_info[0]
        if hourly_rate is None:
            hourly_rate = process_info[1]

    if setup_cost is None:
        setup_cost = 0.0
    if hourly_rate is None:
        hourly_rate = 0.0

    processing_cost_total = setup_cost + (hourly_rate * process_time)

    total_cost = material_cost_total + processing_cost_total

    return {
        "material_cost": round(material_cost_total, 2),
        "processing_cost": round(processing_cost_total, 2),
        "total_cost": round(total_cost, 2),
        "details": {
            "mass_kg": round(mass_kg, 3) if "mass_kg" in locals() else 0,
            "used_density": density,
            "used_material_rate": cost_per_kg,
            "used_setup": setup_cost,
            "used_hourly": hourly_rate,
            "process_time": process_time,
        },
    }
