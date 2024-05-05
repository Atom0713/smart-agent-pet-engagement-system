import asyncio

import requests
from logger import logger
from requests.exceptions import ConnectionError

BASE_URL: str = "http://127.0.0.1:8004"


async def post(url: str, data: dict) -> None:
    url = f"{BASE_URL}{url}"
    try:
        _ = requests.post(url, json=data)
    except ConnectionError:
        logger.info("Data aggregation server is offline! Wait.")
        await asyncio.sleep(60)
