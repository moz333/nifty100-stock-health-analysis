CREATE INDEX idx_profit_loss_id
ON fact_profit_loss(company);

CREATE INDEX idx_profit_loss_year
ON fact_profit_loss(fiscal_year);

CREATE INDEX idx_profit_loss_year_label
ON fact_profit_loss(year_label);