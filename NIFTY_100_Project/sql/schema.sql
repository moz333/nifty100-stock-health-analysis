CREATE DATABASE nifty100;

DROP TABLE IF EXISTS dim_company CASCADE;

CREATE TABLE dim_company (

    id VARCHAR(20) PRIMARY KEY,
    company_logo TEXT,
    company_name TEXT,
    chart_link TEXT,
    about_company TEXT,
    website TEXT,
    nse_profile TEXT,
    bse_profile TEXT,
    face_value NUMERIC,
    book_value NUMERIC,
    roce_percentage NUMERIC,
    roe_percentage NUMERIC
);
DROP TABLE IF EXISTS dim_year CASCADE;
CREATE TABLE dim_year (

    id SERIAL PRIMARY KEY,

    year_label VARCHAR(20),

    fiscal_year INT,

    quarter VARCHAR(10),

    is_ttm BOOLEAN DEFAULT FALSE,

    is_half_year BOOLEAN DEFAULT FALSE,

    sorting_order INT
);
DROP TABLE IF EXISTS dim_sector CASCADE;
CREATE TABLE dim_sector (

    sector_id SERIAL PRIMARY KEY,

    sector_name VARCHAR(100),

    sector_code VARCHAR(20),

    description TEXT
);
DROP TABLE IF EXISTS dim_health_label CASCADE;
CREATE TABLE dim_health_label (

    label_id SERIAL PRIMARY KEY,

    label_name VARCHAR(20),

    min_score NUMERIC,
    max_score NUMERIC,

    color_hex VARCHAR(10)
);
---------------
-- Fact Tables
---------------
DROP TABLE IF EXISTS fact_profit_loss CASCADE;
CREATE TABLE fact_profit_loss (

    id SERIAL PRIMARY KEY,

    company_id VARCHAR(20),

    year VARCHAR(20),
    sales NUMERIC,
    expenses NUMERIC,
    operating_profit NUMERIC,

    opm_percentage NUMERIC,

    other_income NUMERIC,
    interest NUMERIC,
    depreciation NUMERIC,
    profit_before_tax NUMERIC,
    tax_percentage NUMERIC,
    net_profit NUMERIC,
    eps NUMERIC,
    dividend_payout NUMERIC,
	fiscal_year INT,
	sorting_order INT,
	net_profit_margin_pct NUMERIC,
	expense_ratio_pct NUMERIC,
    interest_coverage NUMERIC,
    CONSTRAINT fk_profit_company
        FOREIGN KEY(company_id)
        REFERENCES dim_company(id)
);
DROP TABLE IF EXISTS fact_balance_sheet CASCADE;
CREATE TABLE fact_balance_sheet (

    id SERIAL PRIMARY KEY,

    company_id VARCHAR(20),

    year VARCHAR(20),

    equity_capital NUMERIC,
	
    reserves NUMERIC,

    borrowings NUMERIC,

	other_liabilities NUMERIC,

	total_liabilities NUMERIC,

	fixed_assets NUMERIC,

	cwip NUMERIC,

	investments NUMERIC,
	other_asset NUMERIC,
    total_assets NUMERIC,	
	fiscal_year INT,
 	sorting_order INT,
    debt_to_equity NUMERIC,
    equity_ratio NUMERIC,
    CONSTRAINT fk_balance_company
        FOREIGN KEY(company_id)
        REFERENCES dim_company(id)
);
DROP TABLE IF EXISTS fact_cash_flow CASCADE;
CREATE TABLE fact_cash_flow (

    id SERIAL PRIMARY KEY,

    company_id VARCHAR(20),

    year VARCHAR(20),

    operating_activity NUMERIC,

    investing_activity NUMERIC,

    financing_activity NUMERIC,

    net_cash_flow NUMERIC,

	fiscal_year INT,

	sorting_order INT,

    free_cash_flow NUMERIC,

    CONSTRAINT fk_cashflow_company
        FOREIGN KEY(company_id)
        REFERENCES dim_company(id)
);
DROP TABLE IF EXISTS fact_analysis CASCADE;
CREATE TABLE fact_analysis (

    id SERIAL PRIMARY KEY,

    company_id VARCHAR(20),

    compounded_sales_growth TEXT,

    compounded_profit_growth TEXT,

    stock_price_cagr TEXT,

    roe TEXT,

    CONSTRAINT fk_analysis_company
        FOREIGN KEY(company_id)
        REFERENCES dim_company(id)
);

INSERT INTO dim_company(id)
VALUES ('ZOMATO'), ('VBL'), ('UNITDSPR'), ('UNIONBANK'), ('AGTL'), ('WIPRO'), ('ZYDUSLIFE'), ('ULTRACEMCO'), ('VEDL') ;

--checks

SELECT COUNT(*) FROM dim_company;
SELECT COUNT(*) FROM fact_profit_loss;
SELECT COUNT(*) FROM fact_balance_sheet;
SELECT COUNT(*) FROM fact_cash_flow;

--orphan check

SELECT DISTINCT f.id
FROM fact_profit_loss  f
LEFT JOIN dim_company  d
on f.company_id = d.id
WHERE d.id IS NULL

--NULL metrics

SELECT * FROM fact_profit_loss f
WHERE net_profit IS NULL

--year distribution
SELECT fiscal_year, COUNT(*)
FROM fact_profit_loss
GROUP BY fiscal_year
ORDER BY fiscal_year;