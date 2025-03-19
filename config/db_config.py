# Configuration de postgreSQL 
import psycopg2

DB_CONFIG = {
    "dbname": "toolbox",
    "user": "postgres",
    "password": "ToolBoxPentest",
    "host": "localhost",
    "port": 5433
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)
