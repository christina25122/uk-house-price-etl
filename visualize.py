import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# Connect to Postgres
conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    dbname="uk_data",
    user="uk_user",
    password="uk_pass"
)

query = """
SELECT
  region,
  AVG(average_price) AS avg_price
FROM uk_house_prices
GROUP BY region
ORDER BY avg_price DESC
LIMIT 10;
"""

df = pd.read_sql(query, conn)
conn.close()

# Plot
plt.figure(figsize=(10, 6))
plt.barh(df["region"], df["avg_price"])
plt.xlabel("Average House Price (£)")
plt.title("Top 10 Most Expensive UK Regions")
plt.gca().invert_yaxis()
plt.tight_layout()

# Save image
plt.savefig("top_10_uk_house_prices.png")
plt.show()
