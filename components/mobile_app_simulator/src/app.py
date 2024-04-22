from fastapi import FastAPI

from common.schemas import HttpResponse

app = FastAPI()


@app.get("/")
async def read_root():
    return HttpResponse()
