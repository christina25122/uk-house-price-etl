import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from pathlib import Path

print("=== LOADER STARTED ===")

CSV_PATH = Path("data/clean/ukhpi_average_prices_clean.csv")
print("CSV_PATH =", CSV_PATH.resolve())

if not CSV_PATH.exists():
    raise FileNotFoundError(f"CSV not found: {CSV_PATH.resolve()}")

df = pd.read_csv(CSV_PATH)
print("CSV rows =", len(df))
print("CSV columns =", list(df.columns))

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    dbname="uk_data",
    user="uk_user",
    password="uk_pass",
)
cur = conn.cursor()
print("Connected to Postgres ✅")

cur.execute("""
CREATE TABLE IF NOT EXISTS uk_house_prices (
    date DATE,
    region TEXT,
    average_price NUMERIC
);
""")
print("Table ensured ✅")

cur.execute("TRUNCATE TABLE uk_house_prices;")
print("Table truncated ✅")

rows = list(df[["date", "region", "average_price"]].itertuples(index=False, name=None))
print("Rows to insert =", len(rows))

execute_values(cur,
              "INSERT INTO uk_house_prices (date, region, average_price) VALUES %s",
              rows,
              page_size=10000)

conn.commit()
cur.close()
conn.close()

print("✅ LOADER FINISHED")
