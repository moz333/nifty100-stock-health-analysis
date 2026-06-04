--------------------
-- NULL CHECKS
--------------------

SELECT * FROM fact_profit_loss f
WHERE sales IS NULL

SELECT * FROM fact_profit_loss f
WHERE net_profit IS NULL

SELECT * FROM fact_balance_sheet f
WHERE borrowings IS NULL

SELECT * FROM fact_balance_sheet f
WHERE total_assets IS NULL

SELECT * FROM fact_cash_flow f
WHERE operating_activity IS NULL

SELECT * FROM fact_profit_loss 
WHERE expenses IS NULL

-- DUPLICATES CEHCKS
SELECT id, year, COUNT(*) from fact_profit_loss 
GROUP BY id, year
HAVING COUNT(*)>1

SELECT id, year, COUNT(*) from fact_cash_flow 
GROUP BY id, year
HAVING COUNT(*)>1

SELECT id, COUNT(*) from fact_balance_sheet 
GROUP BY id
HAVING COUNT(*)>1

SELECT id, year, COUNT(*) from fact_analysis 
GROUP BY id, year
HAVING COUNT(*)>1
--foreign key checks

SELECT DISTINCT f.company_id
FROM fact_profit_loss f
LEFT JOIN dim_company d
ON f.company_id = d.id
WHERE d.id IS NULL;

SELECT DISTINCT f.company_id
FROM fact_cash_flow f
LEFT JOIN dim_company d
ON f.company_id = d.id
WHERE d.id IS NULL;

SELECT DISTINCT f.company_id
FROM fact_balance_sheet f
LEFT JOIN dim_company d
ON f.company_id = d.id
WHERE d.id IS NULL;

SELECT DISTINCT f.company_id
FROM fact_analysis f
LEFT JOIN dim_company d
ON f.company_id = d.id
WHERE d.id IS NULL;


--metrics checks

SELECT * FROM fact_profit_loss
WHERE net_profit_margin_pct >1000 and expense_ratio_pct > 1000

SELECT * FROM fact_balance_sheet
WHERE debt_to_equity <0

-- TTM checks
SELECT * FROM fact_profit_loss
WHERE year = 'TTM'


