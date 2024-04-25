from fastapi import FastAPI

from common.schemas import HouseToys, HttpResponse

app = FastAPI()


@app.get("/")
async def read_root():
    return HttpResponse()


@app.get("/toy_activation")
async def show_activated_toys(toys: HouseToys) -> HttpResponse:
    return HttpResponse()


@app.get("/show/schedule")
async def show_toy_activation_schedule() -> HttpResponse:
    return HttpResponse()
