from fastapi import FastAPI
from .schemas import HttpResponse, SensorInput

from .database.table import initialize_db

app = FastAPI()

db = initialize_db()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/collect")
async def collect(sensor_input: SensorInput ) -> HttpResponse:
    return HttpResponse()