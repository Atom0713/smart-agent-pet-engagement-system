import requests

BASE_URL: str = "http://127.0.0.1:8004"


async def post(url: str, data: dict) -> None:
    url = f"{BASE_URL}{url}"
    response = requests.post(url, json=data)
