from aiohttp import ClientSession

BASE_URL: str = "http://127.0.0.1:8000"


async def post(session: ClientSession, url: str, data: dict) -> None:
    url: str = f"{BASE_URL}{url}"
    async with session.post(url, data=data) as response:
        return await response.json()
