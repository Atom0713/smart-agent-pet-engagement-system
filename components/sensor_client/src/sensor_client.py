import asyncio
import datetime

import data_aggregation
from loop import run


async def post_sensor_activation_report() -> None:
    data: dict = {"activated_at": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), "lon": 19, "lat": 18}
    await data_aggregation.post("/collect", data)


async def sensor_client() -> None:
    await post_sensor_activation_report()
    await asyncio.sleep(20)


run(sensor_client)
