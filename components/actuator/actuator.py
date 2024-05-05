import asyncio
import logging
from datetime import datetime

from src.activate import post as activate_toy
from src.models import ActivationSchedule
from src.notify import post as notify_user

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class Activation:
    activate_at: datetime
    toy_name: str
    location: str

    def __init__(self, activate_at: datetime, toy_name: str, location: str) -> None:
        self.activate_at = activate_at
        self.toy_name = toy_name
        self.location = location

    @classmethod
    def from_list(cls, activations: list[dict]):
        return [
            Activation(
                datetime.strptime(activation.get("activate_at", ""), "%m/%d/%Y, %H:%M:%S"),
                activation.get("toy_name", ""),
                activation.get("location", ""),
            )
            for activation in activations
        ]


async def main() -> None:
    while True:
        activations = Activation.from_list(await ActivationSchedule().get_item())
        logger.info(f"Registered {len(activations)} scheduled activations.")
        logger.info("Commencing scheduled activations.")
        for activation in activations:
            logger.info(
                f"Activate_at: {activation.activate_at}, Toy: {activation.toy_name}, Location: {activation.location}"
            )
            if not datetime.now() > activation.activate_at:
                continue
            data: dict = {"toys": [{"name": activation.toy_name, "location": activation.location}]}
            await activate_toy(data)
            await notify_user(data)
        logger.info("Done!")
        await asyncio.sleep(20)


def run() -> None:
    asyncio.run(main())


run()
