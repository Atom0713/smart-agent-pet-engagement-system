import requests

BASE_URL: str = "http://127.0.0.1:8005"


async def post(data: dict) -> None:
    url = f"{BASE_URL}/toy_activation"
    _ = requests.post(url, json=data)
