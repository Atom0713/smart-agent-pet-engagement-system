from aiohttp import ClientSession

BASE_URL: str = (
    "https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{}/lat/{}/data.json"
)


async def get(lon: int, lat: int) -> str:
    async with ClientSession() as session:
        response = await _get(session, BASE_URL.format(lon, lat))
        return response


async def _get(session: ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()
