from fastapi import APIRouter, status, HTTPException
from database import conn, cursor
from schemas import Car

router = APIRouter()

@router.post("/cars", status_code=status.HTTP_201_CREATED)
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
    return {"message": "The car added successfully."}

@router.get("/cars", status_code=status.HTTP_200_OK)
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

@router.get("/cars/{car_id}", status_code=status.HTTP_200_OK)
def get_car(car_id: int):
    cursor.execute("""SELECT * FROM cars WHERE id = ?""", (car_id,))
    car = cursor.fetchone()
    if car is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Car not found")
    return {
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "year": car[3],
            "fuel_type": car[4],
            "power": car[5],
            "max_speed": car[6]
            }

@router.put("/cars/{car_id}", status_code=status.HTTP_200_OK)
def update_car(car_id: int, car: Car):
    cursor.execute("""SELECT * FROM cars WHERE id = ?""", (car_id,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Car not found")
    cursor.execute(
        """UPDATE cars 
        SET brand = ?, model = ?, year = ?, fuel_type = ?, power = ?, max_speed = ? 
        WHERE id = ?""",
        (car.brand, car.model, car.year, car.fuel_type, car.power, car.max_speed, car_id)
        )
    conn.commit()
    return {"message": "Car updated successfully"}

@router.delete("/cars/{car_id}", status_code=status.HTTP_200_OK)
def delete_car(car_id: int):
    cursor.execute("""SELECT * FROM cars WHERE id = ?""", (car_id,))
    result = cursor.fetchone()
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail="Car not found")
    cursor.execute("""DELETE from cars WHERE id = ?""", (car_id,))
    conn.commit()
    return {"message": "Car deleted successfully"}