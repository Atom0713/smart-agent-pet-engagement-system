from fastapi import FastAPI

from common import HouseToy, HouseToys, HttpResponse, logger

app = FastAPI()


@app.get("/")
async def read_root():
    return HttpResponse()


@app.post("/toy_activation")
async def show_activated_toys(house_toys: HouseToys) -> HttpResponse:
    for toy in house_toys.toys:
        logger.info(HouseToy(toy))
    return HttpResponse()


@app.get("/show/schedule")
async def show_toy_activation_schedule() -> HttpResponse:
    return HttpResponse()
