# UK House Price ETL Pipeline

## What this project does
An end-to-end **ETL data pipeline** that processes UK house price data and loads it into PostgreSQL using production-style data engineering practices.

The pipeline:
- cleans and validates raw data,
- enforces data quality checks,
- safely loads data into a database (idempotent upserts),
- runs fully automated using Docker and GitHub Actions.

---

## Architecture (high level)

Raw CSV  
→ Data Cleaning (Python / Pandas)  
→ Data Quality Checks  
→ PostgreSQL (UPSERT, no duplicates)  
→ Visualization  

All components run inside Docker containers.

---

## Tech stack
- Python (Pandas, psycopg2)
- PostgreSQL
- Docker & Docker Compose
- GitHub Actions (CI)
- SQL

---

## Key engineering features
- Environment-based configuration (no hardcoded secrets)
- Data quality checks (fail fast on bad data)
- Idempotent database loads using PRIMARY KEY + UPSERT
- Fully reproducible with one single command
- CI pipeline runs automatically on every push

---

## How to run locally

```bash
docker compose up --build
