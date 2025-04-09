import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="password",
        database="employees_db"
    )

import mysql.connector
import os

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "mysql-service"),
    user=os.getenv("DB_USER", "user"),
    password=os.getenv("DB_PASSWORD", "password"),
    database=os.getenv("DB_NAME", "employees")
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    position VARCHAR(100)
)
""")
conn.commit()