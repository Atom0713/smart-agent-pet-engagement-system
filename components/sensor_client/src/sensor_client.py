import asyncio
import logging
from datetime import datetime
from enum import Enum

import data_aggregation
from loop import run

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class Location(Enum):
    LIVING_ROOM = 1


async def post_sensor_activation_report(now: datetime, lat: int, lon: int, location: int) -> None:
    data: dict = {"activated_at": now.strftime("%m/%d/%Y, %H:%M:%S"), "lon": lon, "lat": lat, "location": location}
    await data_aggregation.post("/collect", data)


async def sensor_client() -> None:
    now: datetime = datetime.now()
    lat: int = 59
    lon: int = 17
    location: int = Location.LIVING_ROOM.value
    logger.info(f"Motion sensor activated. Timestamp: {now}. Lattitude: {lat}, Longitude: {lon}, Location: {location}")
    await post_sensor_activation_report(now, lat, lon, location)
    await asyncio.sleep(20)


run(sensor_client)
