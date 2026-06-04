import pandas as pd
from pathlib import Path

# -----------------------------------
# PATHS
# -----------------------------------

RAW_DIR = "../data/raw"
CLEAN_DIR = "../data/clean"

Path(CLEAN_DIR).mkdir(parents=True, exist_ok=True)

# -----------------------------------
# FILE LIST
# -----------------------------------

files = [
    "analysis.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "companies.xlsx",
    "documents.xlsx",
    "profitandloss.xlsx",
    "prosandcons.xlsx"
]

# -----------------------------------
# READ EXCEL FILES
# -----------------------------------

for file_name in files:

    file_path = f"{RAW_DIR}/{file_name}"

    print(f"\nReading file: {file_name}")

    # Read Excel file
    df = pd.read_excel(file_path, skiprows=1)

    # Create CSV filename
    csv_name = file_name.replace(".xlsx", ".csv")

    output_path = f"{CLEAN_DIR}/{csv_name}"

    # Save as CSV
    df.to_csv(output_path, index=False)

    # Print details
    print(f"Saved CSV: {output_path}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("Column Names:")
    print(list(df.columns))

print("\nAll files processed successfully.")