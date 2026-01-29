import os
import psycopg2

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "uk_data")
DB_USER = os.getenv("DB_USER", "uk_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "uk_pass")

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
