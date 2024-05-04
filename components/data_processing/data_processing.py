import asyncio
import logging
from datetime import datetime, timedelta
from enum import Enum

from src.database import initialize_db
from src.models import ActivationSchedule, SensorActivations

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class Toys(Enum):
    LASER = "laser"


async def convert_data_into_actions(data) -> dict:
    return {}


async def query_aggregated_data() -> list[dict]:
    logger.info("Query sensor activations for last 1 hour.")
    now: datetime = datetime.now()

    sensor_activations: list[dict] = []
    low_value: str = (now - timedelta(hours=1)).strftime("%m/%d/%Y, %H:%M:%S")
    while True:
        response = await SensorActivations().get_item(low_value, now.strftime("%m/%d/%Y, %H:%M:%S"))
        if not response.get("LastEvaluatedKey"):
            break
        low_value = response.get("LastEvaluatedKey", {}).get("activated_at", "")
        sensor_activations = sensor_activations + response.get("Items")

    logger.info(f"Number of sensor activations in 1 hour: {len(sensor_activations)}.")
    return sensor_activations


async def persist_new_actions() -> None:
    ActivationSchedule(activate_at=datetime.now(), toy_name=Toys.LASER.value).save()


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
