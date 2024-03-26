import asyncio

from loop import run


async def sensor_client() -> None:
    # TODO post fake sensory data to the data aggregation tool
    print("Hi.")
    await asyncio.sleep(5)


run(sensor_client)
