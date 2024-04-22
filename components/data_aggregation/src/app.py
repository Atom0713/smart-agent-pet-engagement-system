from fastapi import FastAPI

from common.schemas import HttpResponse, SensorInput
from components.data_aggregation.src import smhi

from .database.table import initialize_db
from .models import SensorActivations

app = FastAPI()

db = initialize_db()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/collect")
async def collect(sensor_input: SensorInput) -> HttpResponse:
    weather_report: str = await smhi.get(sensor_input.lon, sensor_input.lat)
    SensorActivations({"activated_at": sensor_input.activated_at, "weather_report": weather_report}).save()
    return HttpResponse()
