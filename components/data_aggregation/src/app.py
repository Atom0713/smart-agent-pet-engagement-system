from fastapi import FastAPI

from .database.table import initialize_db
from .schemas import HttpResponse, SensorInput

app = FastAPI()

db = initialize_db()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/collect")
async def collect(sensor_input: SensorInput) -> HttpResponse:
    return HttpResponse()
