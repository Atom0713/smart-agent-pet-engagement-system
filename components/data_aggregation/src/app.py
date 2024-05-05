import logging
from enum import Enum

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from common import HttpResponse, SensorInput, logger
from components.data_aggregation.src import smhi

from .database.table import initialize_db
from .models import SensorActivations

app = FastAPI()

db = initialize_db()


class Location(Enum):
    LIVING_ROOM = "1"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
    logging.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/collect")
async def collect(sensor_input: SensorInput) -> HttpResponse:
    logger.info("Sensor activation registered.")
    logger.info(f"Collecting weather data for Lattitude: {sensor_input.lat}, Longitude: {sensor_input.lon}")
    weather_report: str = await smhi.get(sensor_input.lon, sensor_input.lat)
    logger.info("Saving activation metadata to key value store.")
    SensorActivations({**sensor_input.to_dict(), "weather_report": weather_report}).save()
    return HttpResponse()
