import asyncio
import logging

from src.models import ActivationSchedule

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")



async def main() -> None:
    while True:
        response = await ActivationSchedule().get_item()
        logger.info(f"Items: {len(response)}")
        await asyncio.sleep(20)


def run() -> None:
    asyncio.run(main())


run()
