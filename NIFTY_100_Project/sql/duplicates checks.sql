--------------------
--FACT Tables Checks
--------------------

-- fact_profit_loss

SELECT * FROM fact_profit_loss f
WHERE sales IS NULL

SELECT * FROM dim_year

-- delete duplicates from dim_year
DELETE from dim_year a
USING dim_year b
WHERE a.id > b.id
AND a.year_label = b.year_label

UPDATE dim_year
SET year_label =
    SUBSTRING(year_label FROM '(Mar|Jun|Sep|Dec)\s\d{4}')
WHERE year_label <> 'TTM';