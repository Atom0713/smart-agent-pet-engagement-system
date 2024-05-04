import requests

BASE_URL: str = "http://127.0.0.1:8006"


async def post(data: dict) -> None:
    url = f"{BASE_URL}/activate"
    _ = requests.post(url, json=data)
