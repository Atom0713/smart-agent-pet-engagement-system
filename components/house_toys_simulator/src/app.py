from fastapi import FastAPI

from common import HouseToy, HouseToys, HttpResponse, logger

app = FastAPI()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/activate")
async def activate_toy(house_toys: HouseToys) -> HttpResponse:
    for toy in house_toys.toys:
        logger.info(HouseToy(toy))
    return HttpResponse()
