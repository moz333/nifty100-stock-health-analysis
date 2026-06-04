SELECT SUM (sales) total_sales, d.year_label FROM fact_profit_loss f
LEFT JOIN dim_year d
ON f.year = d.year_label
GROUP BY d.year_label, d.sorting_order
HAVING year_label LIKE 'Mar%'
ORDER BY d.sorting_order

SELECT sum(net_profit) FROM fact_profit_loss

SELECT
    y.fiscal_year,

    p.net_profit AS current_year_profit,

    LAG(p.net_profit) OVER (
        ORDER BY y.fiscal_year
    ) AS previous_year_profit,

    ROUND(
        (
            (
                p.net_profit
                -
                LAG(p.net_profit) OVER (
                    ORDER BY y.fiscal_year
                )
            )
            /
            LAG(p.net_profit) OVER (
                ORDER BY y.fiscal_year
            )
        ) * 100,
        2
    ) AS profit_yoy_pct

FROM fact_profit_loss p

JOIN dim_company c
    ON p.company_id = c.id

JOIN dim_year y
    ON p.fiscal_year = y.fiscal_year

WHERE c.company_name = 'Adani Enterprises Ltd'
    AND y.quarter = 'Q4'

ORDER BY y.fiscal_year;

============================
SELECT
    fiscal_year,
    SUM(net_profit) AS total_profit
FROM fact_profit_loss
WHERE fiscal_year IN (2023, 2024)
GROUP BY fiscal_year
ORDER BY fiscal_year;