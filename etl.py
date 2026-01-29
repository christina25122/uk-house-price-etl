import pandas as pd
from pathlib import Path

# ------------------------
# Paths
# ------------------------
RAW_PATH = Path("data/raw/ukhpi_average_prices.csv")
CLEAN_DIR = Path("data/clean")
CLEAN_PATH = CLEAN_DIR / "ukhpi_average_prices_clean.csv"

CLEAN_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------
# Cleaning function
# ------------------------
def clean_data(df):
    df = df.copy()

    possible_sets = [
        ["Date", "Region_Name", "Average_Price"],
        ["Date", "Region Name", "Average Price"],
        ["Date", "RegionName", "AveragePrice"],
    ]

    cols = None
    for s in possible_sets:
        if all(c in df.columns for c in s):
            cols = s
            break

    if cols is None:
        raise ValueError(f"Expected columns not found. Columns present: {list(df.columns)}")

    df = df[cols].copy()
    df.columns = ["date", "region", "average_price"]

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["average_price"] = pd.to_numeric(df["average_price"], errors="coerce")

    df = df.dropna(subset=["date", "region", "average_price"])

    return df

# ------------------------
# Data quality checks
# ------------------------
def run_data_quality_checks(df):
    print("Running data quality checks...")

    if df.empty:
        raise ValueError("Dataset is empty")

    required_columns = ["date", "region", "average_price"]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    if df[required_columns].isnull().any().any():
        raise ValueError("Null values found in critical columns")

    if (df["average_price"] <= 0).any():
        raise ValueError("Non-positive prices found")

    print("Data quality checks PASSED ✅")

# ------------------------
# Main ETL execution
# ------------------------
print("Reading raw CSV...")
df_raw = pd.read_csv(RAW_PATH)
print("Rows loaded:", len(df_raw))
print("Columns found:", list(df_raw.columns))

df_clean = clean_data(df_raw)

run_data_quality_checks(df_clean)

df_clean.to_csv(CLEAN_PATH, index=False)
print("Clean data saved to:", CLEAN_PATH)
print(df_clean.head())

print("ETL completed successfully ✅")
