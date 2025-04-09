from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_db_connection

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Employee(BaseModel):
    name: str
    email: str
    position: str

@app.post("/employees")
def add_employee(emp: Employee):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO employees (name, email, position) VALUES (%s, %s, %s)", 
                   (emp.name, emp.email, emp.position))
    db.commit()
    cursor.close()
    db.close()
    return {"message": "Employee added"}

@app.get("/employees")
def list_employees():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
