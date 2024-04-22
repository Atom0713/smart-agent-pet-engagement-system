from fastapi import FastAPI

from common.schemas import HouseToys, HttpResponse

app = FastAPI()


@app.get("/")
async def read_root() -> HttpResponse:
    return HttpResponse()


@app.post("/activate")
async def activate_toy(house_toys: HouseToys) -> HttpResponse:
    return HttpResponse()
