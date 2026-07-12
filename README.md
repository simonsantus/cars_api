# Cars API
Simple REST API built with FastAPI and SQLite.

This project demonstrates CRUD operations, REST API design, request validation using Pydantic and SQLite database integration.

## Features
- Get all cars
- Get car by ID
- Add a new car
- Update a car
- Delete a car
- Request validation with Pydantic
- SQLite database integration
- HTTP status codes 
- Error handling

## Technologies
- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Project structure
```
cars_api/
|
|--main.py
|--database.py
|--routers_cars.py
|--schemas.py
|--requirements.txt
|--README.md
|--LICENSE
|--.gitignore
|--cars.db
```

## Run project
Install dependencies

```bash
pip install -r requirements.txt
```

Run server

```bash
uvicorn main:app --reload
```

## API documentation
Open in your browser:
```
http://127.0.0.1:8000/docs
```

## Available Endpoints

| Method | Endpoint       | Description
|  GET   | /cars          | Get all cars
|  GET   | /cars/{car_id} | Get one car
| POST   | /cars          | Create a new car
|  PUT   | /cars/{car_id} | Update a car
| DELETE | /cars/{car_id} | Delete a cars

## License

MIT License