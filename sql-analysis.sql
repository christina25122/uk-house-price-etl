-- Top 10 most expensive regions
SELECT
  region,
  AVG(average_price) AS avg_price,
  RANK() OVER (ORDER BY AVG(average_price) DESC) AS price_rank
FROM uk_house_prices
GROUP BY region
ORDER BY price_rank
LIMIT 10;

-- Year-over-year price change
SELECT
  region,
  date,
  average_price,
  LAG(average_price, 12) OVER (
    PARTITION BY region
    ORDER BY date
  ) AS price_last_year,
  average_price - LAG(average_price, 12) OVER (
    PARTITION BY region
    ORDER BY date
  ) AS yearly_change
FROM uk_house_prices;
