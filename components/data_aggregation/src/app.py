from fastapi import FastAPI

from .database.table import initialize_db
from .models import SensorActivations
from .schemas import HttpResponse, SensorInput

app = FastAPI()

db = initialize_db()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/collect")
async def collect(sensor_input: SensorInput) -> HttpResponse:
    _ = SensorActivations({"activated_at": sensor_input.activated_at}).save()
    return HttpResponse()
