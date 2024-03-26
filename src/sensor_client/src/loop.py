import asyncio


async def main(sensor_client) -> None:
    while True:
        await sensor_client()


def run(sensor_client) -> None:
    asyncio.run(main(sensor_client))
