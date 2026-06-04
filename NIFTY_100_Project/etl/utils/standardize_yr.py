import re
import pandas as pd

def standardise_yr(year_value):
    
    if pd.isna(year_value):
        return None
    
    year_value = str(year_value).strip ()
    
    if year_value == "TTM":
        return "TTM"
    
    ex =re.match(r"([A-Za-z]{3})-(\d{2})", year_value)
    
    if ex:
        month = ex.group(1)
        year = 2000 + int( ex.group(2))
        
        return f"{month} {year}"
    
    return year_value

def extract_fiscal_year(year_label):
    
    if pd.isna(year_label):
        return None
    elif year_label == "TTM":
        return None
    
    ex = re.search(r"(\d{4})", year_label)
    if ex:
            return int(ex.group (1) )
    else:
        return None
        
def sortingOrder(year_label):
     
    fiscal_year = extract_fiscal_year(year_label)
    
    if fiscal_year is None:
        return 9999
    
    return fiscal_year 

        
    



    