import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

conn = sqlite3.connect("cars.db", check_same_thread=False)
cursor = conn.cursor()
app = FastAPI()

class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    fuel_type: str
    power: int
    max_speed: int

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
id INTEGER PRIMARY KEY, 
brand TEXT,
model TEXT,
year INTEGER,
fuel_type TEXT,
power INTEGER,
max_speed INTEGER
)
""")
conn.commit()

@app.post("/cars")
def add_car(car: Car):
    cursor.execute(
        """INSERT INTO cars
        (id, brand, model, year, fuel_type, power, max_speed) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, 
    (
        car.id, 
        car.brand, 
        car.model, 
        car.year, 
        car.fuel_type, 
        car.power, 
        car.max_speed
        )
        )
    conn.commit()
    return {"message": "The car has been added to the database."}