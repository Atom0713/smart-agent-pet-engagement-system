import asyncio

from .models import SensorActivations, TempModel


async def convert_data_into_actions(data) -> dict:
    return {}


async def query_aggregated_data() -> dict:
    _ = await SensorActivations().get_item()
    return {}


async def persist_new_actions(actions) -> None:
    TempModel(actions).save()


async def main() -> None:
    while True:
        await asyncio.sleep(20)
        data = await query_aggregated_data()
        actions = await convert_data_into_actions(data)
        await persist_new_actions(actions)


def run() -> None:
    asyncio.run(main())


run()
