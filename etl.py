import pandas as pd
from pathlib import Path

raw_file = Path("data/raw/ukhpi_average_prices.csv")
clean_dir = Path("data/clean")
clean_dir.mkdir(parents=True, exist_ok=True)

print("Reading CSV file...")
df = pd.read_csv(raw_file)

print("Columns found:", list(df.columns))
print("Rows loaded:", len(df))

# The Land Registry HPI CSV usually includes these columns (sometimes slightly different)
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
    raise ValueError("I couldn't find the expected columns. Copy/paste the 'Columns found' list here.")

clean_df = df[cols].copy()
clean_df.columns = ["date", "region", "average_price"]

clean_df["date"] = pd.to_datetime(clean_df["date"], errors="coerce")
clean_df["average_price"] = pd.to_numeric(clean_df["average_price"], errors="coerce")
clean_df = clean_df.dropna()

clean_file = clean_dir / "ukhpi_average_prices_clean.csv"
clean_df.to_csv(clean_file, index=False)

print("CLEAN DATA SAVED TO:", clean_file)
print(clean_df.head())
