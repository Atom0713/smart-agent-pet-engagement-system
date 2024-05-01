from fastapi import FastAPI

from common import HouseToys, HttpResponse, logger

app = FastAPI()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/activate")
async def activate_toy(house_toys: HouseToys) -> HttpResponse:
    logger.info(f"Activating: {house_toys}")
    return HttpResponse()
