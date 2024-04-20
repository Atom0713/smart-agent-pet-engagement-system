import asyncio

import aiohttp
import data_aggregation
from loop import run


async def post_sensor_activation_report(data: dict) -> None:
    async with aiohttp.ClientSession() as session:
        response = await data_aggregation.post(session, "/collect", data)
        print(response)


async def sensor_client() -> None:
    await asyncio.sleep(20)
    data: dict = {}
    await post_sensor_activation_report(data)


run(sensor_client)
