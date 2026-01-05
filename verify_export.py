import costs
import utils.export as export
from unittest.mock import patch
import io
import pandas as pd


def test_export_logic():
    print("Testing Export Generation...")

    # Mock Data
    config = {
        "quantity": 10,
        "material": "Test Metal",
        "cutting": "Test Cutting",
        "machining": True,  # Boolean process
        "finishing": "Test Finish",
    }
    volume_in3 = 2.5
    overrides = {}

    # Mock data loader returns
    # material: density 0.1, cost $5.00/lb
    # cutting: setup 10, rate $100, run 5
    # machining: setup 20, rate $150, run 30
    # finishing: setup 0, rate $50, run 10

    def mock_get_material(name):
        return (0.1, 5.0)  # density, cost

    def mock_get_process_rates(name):
        if name == "Test Cutting":
            return (10, 100, 5)  # setup, rate, run
        if name == "Machining":
            return (20, 150, 30)
        if name == "Test Finish":
            return (0, 50, 10)
        return None

    with patch("costs.get_material_rate", side_effect=mock_get_material):
        with patch("costs.get_process_rates", side_effect=mock_get_process_rates):
            # 1. Calculate Breakdown
            print("\nCalculating breakdown...")
            result = costs.calculate_part_breakdown(config, volume_in3, overrides)

            print(f"Total Batch Cost: {result['total_cost_batch']}")

            # Expected calculations:
            # Material: 2.5 * 0.1 = 0.25 lbs. Cost = 0.25 * 5.0 * 10 = $12.50
            # Cutting: Setup (10*100/60) = 16.67. Run (5*100/60)*10 = 83.33. Total = 100.00
            # Machining: Setup (20*150/60) = 50.00. Run (30*150/60)*10 = 750.00. Total = 800.00
            # Finish: Setup 0. Run (10*50/60)*10 = 83.33. Total = 83.33
            # Grand Total: 12.5 + 100 + 800 + 83.33 = 995.83

            # 2. Prepare Export Data
            export_data = [{"name": "Part A", "config": config, "result": result}]

            # 3. Generate CSV
            print("\nGenerating CSV...")
            csv_string = export.generate_batch_export(export_data)

            print("CSV Output Preview:")
            print(csv_string)

            # 4. Verify Columns
            df = pd.read_csv(io.StringIO(csv_string))

            required_cols = [
                "Part Name",
                "Quantity",
                "Material",
                "Total Batch Cost ($)",
                "Cost: Material: Test Metal ($)",
                "Cost: Test Cutting ($)",
                "Cost: Machining ($)",
                "Cost: Test Finish ($)",
            ]

            missing = [c for c in required_cols if c not in df.columns]
            if not missing:
                print("\nSUCCESS: All required columns present.")
            else:
                print(f"\nFAILURE: Missing columns: {missing}")

            val = df.iloc[0]["Total Batch Cost ($)"]
            if abs(val - 995.83) < 0.1:
                print("SUCCESS: Total cost matches expected.")
            else:
                print(f"FAILURE: Total cost {val} != 995.83")


if __name__ == "__main__":
    test_export_logic()
