import os
from pathlib import Path

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values


def main():
    print("=== LOADER STARTED ===")

    # -------------------------
    # File paths
    # -------------------------
    CSV_PATH = Path("data/clean/ukhpi_average_prices_clean.csv")
    print("CSV_PATH =", CSV_PATH.resolve())

    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV not found: {CSV_PATH.resolve()}")

    df = pd.read_csv(CSV_PATH)
    print("CSV rows =", len(df))
    print("CSV columns =", list(df.columns))

    # Basic guard (extra safety)
    required_cols = ["date", "region", "average_price"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in cleaned CSV: {missing}")

    # -------------------------
    # DB config (from env)
    # -------------------------
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = int(os.getenv("DB_PORT", "5432"))
    DB_NAME = os.getenv("DB_NAME", "uk_data")
    DB_USER = os.getenv("DB_USER", "uk_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "uk_pass")

    print(f"Connecting to Postgres at {DB_HOST}:{DB_PORT} db={DB_NAME} user={DB_USER}")

    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    cur = conn.cursor()
    print("Connected to Postgres ✅")

    # -------------------------
    # Create table with PRIMARY KEY
    # (date, region) uniquely identifies each record
    # -------------------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS uk_house_prices (
        date DATE NOT NULL,
        region TEXT NOT NULL,
        average_price NUMERIC,
        PRIMARY KEY (date, region)
    );
    """)
    print("Table ensured with PRIMARY KEY ✅")

    # -------------------------
    # Prepare rows
    # -------------------------
    rows = list(df[["date", "region", "average_price"]].itertuples(index=False, name=None))
    print("Rows to upsert =", len(rows))

    # -------------------------
    # UPSERT (safe to rerun)
    # -------------------------
    upsert_sql = """
    INSERT INTO uk_house_prices (date, region, average_price)
    VALUES %s
    ON CONFLICT (date, region)
    DO UPDATE SET average_price = EXCLUDED.average_price;
    """

    execute_values(cur, upsert_sql, rows, page_size=10000)
    conn.commit()
    print("Upsert committed ✅")

    # Quick verification (optional but useful)
    cur.execute("SELECT COUNT(*) FROM uk_house_prices;")
    count = cur.fetchone()[0]
    print("Rows currently in DB =", count)

    cur.close()
    conn.close()
    print("✅ LOADER FINISHED")


if __name__ == "__main__":
    main()

