import asyncio

from .models import SensorActivations, TempModel


async def convert_data_into_actions(data) -> None:
    pass


async def query_aggregated_data() -> None:
    _ = await SensorActivations.get_item()


async def persist_new_actions(actions) -> None:
    TempModel(actions).save()


async def main() -> None:
    while True:
        await asyncio.sleep(20)
        data = await query_aggregated_data()
        actions = convert_data_into_actions(data)
        persist_new_actions(actions)


def run() -> None:
    asyncio.run(main())
