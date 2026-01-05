import data_loader
import pandas as pd

try:
    print("Fetching processes data...")
    df = data_loader.get_processes()
    print("Columns found:")
    for col in df.columns:
        print(f"- {col}")

    if "run_time_mins" in df.columns:
        print("\nSUCCESS: 'run_time_mins' column found.")
        print("Sample data (head):")
        print(df[["name", "run_time_mins"]].head())
    else:
        print("\nFAILURE: 'run_time_mins' column NOT found.")

except Exception as e:
    print(f"\nError occurred: {e}")
