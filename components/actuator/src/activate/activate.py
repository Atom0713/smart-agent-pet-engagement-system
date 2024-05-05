import asyncio

import requests
from requests.exceptions import ConnectionError
from src.logger import logger

BASE_URL: str = "http://127.0.0.1:8006"


async def post(data: dict) -> None:
    url = f"{BASE_URL}/activate"

    try:
        _ = requests.post(url, json=data)
    except ConnectionError:
        logger.info("Activation failed, device is offline!")
        await asyncio.sleep(60)
