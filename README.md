\# UK House Price ETL Pipeline 🇬🇧



\## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline built using UK Government open data.



The pipeline downloads UK House Price Index data, cleans and transforms it using Python and pandas, and loads it into a PostgreSQL database running inside Docker. The final dataset is queried using SQL for analysis.



This project demonstrates real-world data engineering skills, including debugging, data cleaning, containerisation, and database loading.



---



\## Tech Stack

\- Python 3.12

\- pandas

\- PostgreSQL 15

\- Docker

\- SQL

\- UK Government Open Data (Land Registry)



---



\## Project Architecture



1\. \*\*Extract\*\*

&nbsp;  - Source: UK Land Registry House Price Index (CSV)

&nbsp;  - Data stored in `data/raw/`



2\. \*\*Transform\*\*

&nbsp;  - Cleaned columns (date, region, average\_price)

&nbsp;  - Handled missing values

&nbsp;  - Standardised data types

&nbsp;  - Output saved to `data/clean/`



3\. \*\*Load\*\*

&nbsp;  - PostgreSQL database running in Docker

&nbsp;  - Table: `uk\_house\_prices`

&nbsp;  - Data loaded using PostgreSQL `COPY` command



---



\## How to Run



\### 1. Start PostgreSQL with Docker

```bash

docker run --name uk\_postgres \\

&nbsp; -e POSTGRES\_USER=uk\_user \\

&nbsp; -e POSTGRES\_PASSWORD=uk\_pass \\

&nbsp; -e POSTGRES\_DB=uk\_data \\

&nbsp; -p 5432:5432 \\

&nbsp; -d postgres:15



