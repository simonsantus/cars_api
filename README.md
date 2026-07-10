# Cars API
Simple REST API built with FastAPI and SQLite.

## Features
- Get all cars
- Get car by ID
- Add a new car
- Update a car
- Delete a car

## Technologies
- Python
- FastAPI
- SQLite
- Pydantic

## Project structure
```
cars_api/
|
|--main.py
|--database.py
|--routers_cars.py
|--schemas.py
|--README.md
```

## Run project
```bash
uvicorn main:app --reload
```

## API documentation
Open in your browser:
```
http://127.0.0.1:8000/docs
```