# 🇬🇧 UK House Price ETL Pipeline

## 📌 Project Overview
This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using UK Government open data from the UK Land Registry House Price Index.

The pipeline extracts raw data, cleans and transforms it using Python and pandas, loads it into a PostgreSQL database running in Docker, and performs analytical SQL queries using window functions.

This project is designed as a portfolio project for the UK data job market.

---

## 🏗️ Architecture

Raw CSV  
↓  
Python ETL (pandas)  
↓  
Clean CSV  
↓  
PostgreSQL (Docker)  
↓  
SQL Analysis  

---

## 🛠️ Tech Stack

- Python 3.12  
- pandas  
- PostgreSQL 15  
- Docker  
- SQL (Window Functions)  
- UK Government Open Data  

---

## 📂 Project Structure
uk-house-price-etl/
├── data/
│ ├── raw/ # Raw government data (ignored in Git)
│ └── clean/ # Cleaned CSV output (ignored in Git)
├── etl.py
├── load_to_postgres.py
├── sql/
│ └── analysis.sql
├── README.md
└── .gitignore


---

## 🔄 ETL Pipeline

### Extract
- Source: UK Land Registry House Price Index (CSV)
- Stored in `data/raw/`

### Transform
- Selected columns:
  - date
  - region
  - average_price
- Cleaned and validated data
- Output written to `data/clean/ukhpi_average_prices_clean.csv`

### Load
- PostgreSQL database running in Docker
- Table name: `uk_house_prices`
- Data loaded using PostgreSQL COPY command

---

## 🗄️ Database Schema

```sql
CREATE TABLE uk_house_prices (
  date DATE,
  region TEXT,
  average_price NUMERIC
);


📊 Example SQL Analysis

Top 10 Most Expensive Regions
SELECT
  region,
  AVG(average_price) AS avg_price,
  RANK() OVER (ORDER BY AVG(average_price) DESC) AS price_rank
FROM uk_house_prices
GROUP BY region
ORDER BY price_rank
LIMIT 10;

Year-over-Year Price Change
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

🎯 Skills Demonstrated

End-to-end ETL pipeline development

Python data processing with pandas

PostgreSQL and SQL window functions

Docker containerisation

Git & GitHub version control

👤 Author

Loshni Christina
GitHub: https://github.com/christina25122

