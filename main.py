from fastapi import FastAPI
from routers_cars import router

app = FastAPI()

app.include_router(router)