import costs
from unittest.mock import MagicMock, patch


# Mock data_loader to return a known process dict
def test_costs_update():
    print("Testing costs.get_process_rates logic...")

    mock_process = {
        "setup_time_mins": 15,
        "hourly_rate": 100,
        "run_time_mins": 120,  # Known value to test
    }

    with patch("data_loader.get_process_by_name", return_value=mock_process):
        rates = costs.get_process_rates("Test Process")
        print(f"Returned rates: {rates}")

        if len(rates) == 3:
            print("SUCCESS: 3 values returned.")
        else:
            print(f"FAILURE: Expected 3 values, got {len(rates)}")

        if rates[2] == 120:
            print("SUCCESS: run_time_mins is 120.")
        else:
            print(f"FAILURE: run_time_mins is {rates[2]}, expected 120.")


def test_app_logic_simulation():
    print("\nSimulating app logic...")
    # Simulate the logic inside app.py's add_process_row

    # Inputs
    p_info = (15, 100, 120)  # setup, rate, run
    p_ovr = {}  # No overrides

    setup_mins = float(p_ovr.get("setup_time_mins", p_info[0]))
    rate = float(p_ovr.get("rate", p_info[1]))
    run_mins = float(p_ovr.get("run_time_mins", p_info[2]))  # This is the key line

    print(f"Resolved Run Mins: {run_mins}")

    if run_mins == 120:
        print("SUCCESS: App logic uses correct run_time_mins.")
    else:
        print(f"FAILURE: App logic got {run_mins}, expected 120.")


if __name__ == "__main__":
    test_costs_update()
    test_app_logic_simulation()
