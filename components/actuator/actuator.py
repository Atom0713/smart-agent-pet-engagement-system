import asyncio
import logging

from src.models import ActivationSchedule
from src.notify import post as notify_user
from src.activate import post as activate_toy

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")



async def main() -> None:
    while True:
        response = await ActivationSchedule().get_item()
        logger.info(f"Items: {len(response)}")
        await activate_toy({"toys": [{"name": "laser"}]})
        await notify_user({"toys": [{"name": "laser"}]})
        await asyncio.sleep(20)


def run() -> None:
    asyncio.run(main())


run()
