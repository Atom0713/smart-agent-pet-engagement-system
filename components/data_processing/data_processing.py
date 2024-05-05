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


class Location(Enum):
    LIVING_ROOM = 1


class Activation:
    activate_at: datetime
    toy_name: str
    location: str

    def __init__(self, activate_at: datetime, toy_name: str, location: str) -> None:
        self.activate_at = activate_at
        self.toy_name = toy_name
        self.location = location

    def to_dict(self) -> dict:
        return dict(
            activate_at=self.activate_at.strftime("%m/%d/%Y, %H:%M:%S"), toy_name=self.toy_name, location=self.location
        )


async def convert_data_into_actions(data) -> list[Activation]:
    logger.info("Convert aggregated data into actions.")
    return [Activation(datetime.now(), Toys.LASER.value, Location.LIVING_ROOM.name)]


async def query_aggregated_data() -> list[dict]:
    logger.info("Query sensor activations for last 1 hour.")
    now: datetime = datetime.now()

    sensor_activations: list[dict] = []
    low_value: str = (now - timedelta(hours=1)).strftime("%m/%d/%Y, %H:%M:%S")
    while True:
        response = await SensorActivations().get_item(
            low_value, now.strftime("%m/%d/%Y, %H:%M:%S"), Location.LIVING_ROOM.name
        )
        if not response.get("LastEvaluatedKey"):
            break
        low_value = response.get("LastEvaluatedKey", {}).get("activated_at", "")
        sensor_activations = sensor_activations + response.get("Items")

    logger.info(f"Number of sensor activations in 1 hour: {len(sensor_activations)}.")
    return sensor_activations


async def persist_new_activations(actions: list[Activation]) -> None:
    logger.info("Persist derived actions.")
    for activation in actions:
        await ActivationSchedule(activation.to_dict()).save()


async def main() -> None:
    while True:
        data = await query_aggregated_data()
        actions = await convert_data_into_actions(data)
        await persist_new_activations(actions)
        await asyncio.sleep(50)


def run() -> None:
    initialize_db()
    asyncio.run(main())


run()
