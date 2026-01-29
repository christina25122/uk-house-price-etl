# UK House Price ETL Pipeline

## What this project does
This project implements an end-to-end ETL data pipeline that processes UK house price data and loads it into PostgreSQL using production-style data engineering practices.

The pipeline:
- cleans and validates raw data  
- enforces data quality checks  
- safely loads data into a database using idempotent upserts  
- runs fully automated using Docker and GitHub Actions  

---

## How to run locally
```bash
docker compose up --build

---

Architecture

Raw CSV
→ Data cleaning (Python / Pandas)
→ Data quality checks
→ PostgreSQL (UPSERT, no duplicates)
→ Visualization

All components run inside Docker containers.

Tech stack

-Python (Pandas, psycopg2)
-PostgreSQL
-Docker and Docker Compose
-GitHub Actions (CI)
-SQL

Key engineering features

-Environment-based configuration (no hardcoded secrets)
-Data quality checks with fail-fast validation
-Idempotent database loads using primary keys and UPSERT
-Fully reproducible pipeline with a single command
-Continuous integration running on every pushtion pipeline that runs automatically on every push
