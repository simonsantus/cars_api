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

@app.get("/cars")
def get_cars():
    cursor.execute("""SELECT * FROM cars""")
    cars = cursor.fetchall()
    result = []
    for car in cars:
        result.append({
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "year": car[3],
            "fuel_type": car[4],
            "power": car[5],
            "max_speed": car[6]
            })
    return result

@app.get("/cars/{car_id}")
def get_car(car_id: int):
    cursor.execute("""SELECT * FROM cars WHERE id = ?""", (car_id,))
    car = cursor.fetchone()
    if car is None:
        return {"message": "Car not found"}
    return {
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "year": car[3],
            "fuel_type": car[4],
            "power": car[5],
            "max_speed": car[6]
            }