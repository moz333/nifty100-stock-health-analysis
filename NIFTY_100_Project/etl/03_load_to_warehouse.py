import pandas as pd
from utils.db import engine

# -----------------------------------
# PATHS
# -----------------------------------

TRANSFORMED_DIR = "../data/transformed"

# -----------------------------------
# FILE MAPPING
# -----------------------------------

table_mapping = {

    "companies.csv": "dim_company",

    "profitandloss.csv": "fact_profit_loss",

    "balancesheet.csv": "fact_balance_sheet",

    "cashflow.csv": "fact_cash_flow",

    "analysis.csv": "fact_analysis"
}
fl_path = f"{TRANSFORMED_DIR}/companies.csv"
year_files = ["balancesheet.csv", "cashflow.csv", "profitandloss.csv"]
company_df = pd.read_csv(fl_path)
missing_companies = set()
unique_companies = set(company_df["id"].unique())

#------------------------------------
# missing companies
#-----------------------------------

for file_name in year_files:

    file_path = f"{TRANSFORMED_DIR}/{file_name}"

    df = pd.read_csv(file_path)

    all_companies = set(df["company_id"].unique())

    missing_companies.update(all_companies - unique_companies)

print(missing_companies)
    
# -----------------------------------
# LOAD LOOP
# -----------------------------------

for file_name in table_mapping:
    
    if file_name in year_files:
        
        all_years = []
        
        file_path = f"{TRANSFORMED_DIR}/{file_name}"
        
        for file_name in year_files:
            
            df = pd.read_csv (file_path);
            
            df_yr = df[["year", "fiscal_year", "sorting_order"]]
            
            all_years.append (df_yr)
        
        
        dim_year_df = pd.concat(all_years)
        
        dim_year_df.drop_duplicates (inplace = True)
        
        dim_year_df = dim_year_df.rename (columns = {"year": "year_label"})
        
        dim_year_df["is_ttm"] = dim_year_df["year_label"].str.upper() .eq("TTM")
        
        # load to Database
        
        dim_year_df.to_sql (name = "dim_year", con=engine, if_exists="append", index=False)
    else:
        continue

for file_name, table_name in table_mapping.items():

    file_path = f"{TRANSFORMED_DIR}/{file_name}"

    print(f"\nLoading {file_name} → {table_name}")

    # Read CSV
    
    df = pd.read_csv(file_path)

    # Load to PostgreSQL
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} rows into {table_name}")

print("\nWarehouse loading completed successfully.")