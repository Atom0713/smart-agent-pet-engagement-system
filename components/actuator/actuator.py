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

    def __init__(self, activate_at: datetime, toy_name: str) -> None:
        self.activate_at = activate_at
        self.toy_name = toy_name

    @classmethod
    def from_list(cls, activations: list[dict]):
        return [
            Activation(
                datetime.strptime(activation.get("activate_at", ""), "%m/%d/%Y, %H:%M:%S"),
                activation.get("toy_name", ""),
            )
            for activation in activations
        ]


async def main() -> None:
    while True:
        activations = Activation.from_list(await ActivationSchedule().get_item())
        logger.info(f"Registered {len(activations)} scheduled activations.")
        logger.info("Commencing scheduled activations.")
        for activation in activations:
            logger.info(f"Activate_at: {activation.activate_at}, Toy: {activation.toy_name}")
            if not datetime.now() > activation.activate_at:
                continue
            await activate_toy({"toys": [{"name": activation.toy_name}]})
            await notify_user({"toys": [{"name": activation.toy_name}]})
        logger.info("Done!")
        await asyncio.sleep(20)


def run() -> None:
    asyncio.run(main())


run()
