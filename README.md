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

## Architecture
Data flow:

Raw CSV  
→ Data cleaning (Python / Pandas)  
→ Data quality checks  
→ PostgreSQL (UPSERT, no duplicate records)  
→ Visualization  

The entire pipeline runs inside Docker containers and is orchestrated using Docker Compose.

---

## Tech stack
- Python (Pandas, psycopg2)
- PostgreSQL
- Docker and Docker Compose
- GitHub Actions for CI
- SQL

---

## Key engineering features
- Environment-based configuration for database connectivity
- Data quality checks that fail the pipeline on invalid data
- Idempotent database loads using primary keys and UPSERT logic
- Fully reproducible execution with a single Docker command
- Continuous integration pipeline that runs automatically on every push
