import pandas as pd
from pathlib import Path
import numpy as np
from utils.standardize_yr import (standardise_yr, extract_fiscal_year, sortingOrder)
import os

SRC_PATH = "../data/clean"
DST_PATH = "../data/transformed"

Path(DST_PATH).mkdir(parents=True, exist_ok=True)

# -----------------------------------
# CLEAR OLD TRANSFORMED FILES
# -----------------------------------

for file in os.listdir(DST_PATH):

    if file.endswith(".csv"):

        os.remove(f"{DST_PATH}/{file}")

print("Old transformed files removed.")

files = [
    "analysis.csv",
    "balancesheet.csv",
    "cashflow.csv",
    "companies.csv",
    "documents.csv",
    "profitandloss.csv",
    "prosandcons.csv"
]

for file_name in files:
    
    file_path = f"{SRC_PATH}/{file_name}"
    print (f"\nprocessing file: {file_name}")
    
    df = pd.read_csv (file_path)
    
    df.columns = ( df.columns
                  .str.strip ()
                  .str.lower ()
                  .str.replace (" ", "_", regex= False)
                  )
    
    df.replace (["Null", "null", " ", "NULL", ""], np.nan, inplace= True)
    
    df = df.apply (
        lambda col: col.str.strip ()
        if col.dtype == "object"
        else col
    )
    
    #year standardising
    
    if file_name in [   "balancesheet.csv", "cashflow.csv", "profitandloss.csv"]:
        
        df["year"] = df["year"].apply (standardise_yr)
        
        df["fiscal_year"] = df["year"].apply (extract_fiscal_year)
        
        df["sorting_order"] = df["year"].apply (sortingOrder) 
    
    elif file_name == "documents.csv":
        
        df["fiscal_year"] = df["year"]
        
        df["sorting_order"] = df["year"]
        
    #------------------------------------
    # Metrics Calculation
    #------------------------------------
    if file_name == "balancesheet.csv":
        
        numeric_cols = [
        "equity_capital",
        "reserves",
        "borrowings",
        "total_assets"
        ]
    
        for col in numeric_cols:
            df[col] = pd.to_numeric( df[col], errors="coerce")
            
        #---------------------
        # debt to equity
        #---------------------
        df["debt_to_equity"] = np.where(
        (df["equity_capital"] + df["reserves"]) != 0,
        df["borrowings"] / (df["equity_capital"] + df["reserves"]),
        np.nan )
        
        # -----------------------------------
        # EQUITY RATIO
        # -----------------------------------

        df["equity_ratio"] = np.where(
        df["total_assets"] != 0,
        (df["equity_capital"] + df["reserves"]) / df["total_assets"],
        np.nan)
            
    elif file_name == "profitandloss.csv":
        
        numeric_cols = [
        "sales",
        "expenses",
        "operating_profit",
        "opm_percentage",
        "other_income",
        "interest",
        "depreciation",
        "profit_before_tax",
        "tax_percentage",
        "net_profit",
        "eps",
        "dividend_payout"
        ]
        
        for col in numeric_cols:
            df[col] = pd.to_numeric (df[col], errors="coerce")
            
        #-----------------------
        # Net profit margin
        #-----------------------
        
        df["net_profit_margin_pct"] = np.where(df["sales"]!=0, (df["net_profit"]/df["sales"])*100, np.nan)
        
        #-----------------------
        # expense_ratio_pct
        #-----------------------
        
        df["expense_ratio_pct"] = np.where(df["sales"] != 0,   (df["expenses"]  /df["sales"]) * 100,np.nan)        
        
        #----------------------
        # expense ratio
        #----------------------
        
        df["expense_ratio_pct"] = np.where(
    df["sales"] != 0,
    (df["expenses"] / df["sales"]) * 100,
    np.nan
)
        
        # interest coverage
        
        df["interest_coverage"] = np.where(
    df["interest"] != 0,
    df["operating_profit"] / df["interest"],
    np.nan
)
        
    elif file_name == "cashflow.csv":
            
        numeric_cols = ["operating_activity", "investing_activity"]
            
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        
        # free cash flow
        
        
        df["free_cash_flow"] = (
    df["operating_activity"] +
    df["investing_activity"]
) 
        
    output_path = f"{DST_PATH}/{file_name}"
    
    df.to_csv(output_path,index = False)
    
    print (f"{file_name} processing completed.\n")
    print (f"saved transformed files in:{output_path}\n")
    print (f"number of rows: {df.shape[0]}\n")
    print (f"number of columns: {df.shape[1]}\n")
    
print ("All files transformed successfully!!\n")
           
    