import asyncio
import datetime
import logging
from enum import Enum

from src.database import initialize_db
from src.models import ActivationSchedule, SensorActivations

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class Toys(Enum):
    LASER = "laser"


async def convert_data_into_actions(data) -> dict:
    return {}


async def query_aggregated_data() -> dict:
    logger.info("Query sensor activations.")
    sensor_activations = await SensorActivations().get_item()
    logger.info(f"Number of sensor activations: {len(sensor_activations.get('Items'))}")
    return sensor_activations


async def persist_new_actions() -> None:
    ActivationSchedule(activate_at=datetime.datetime.now(), toy_name=Toys.LASER.value).save()


async def main() -> None:
    while True:
        data = await query_aggregated_data()
        _ = await convert_data_into_actions(data)
        await persist_new_actions()
        await asyncio.sleep(20)


def run() -> None:
    initialize_db()
    asyncio.run(main())


run()
