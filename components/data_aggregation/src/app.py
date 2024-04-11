from fastapi import FastAPI

from .database.table import initialize_db

app = FastAPI()

db = initialize_db()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
