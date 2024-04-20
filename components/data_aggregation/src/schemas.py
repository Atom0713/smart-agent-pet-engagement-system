from enum import Enum
from typing import Literal

from pydantic import BaseModel


class Status(Enum):
    OK: str = "OK"
    ERROR: str = "ERROR"


class HttpResponse(BaseModel):
    status: Literal[Status.OK, Status.ERROR] = Status.OK
    data: dict = {}


class SensorInput(BaseModel):
    activated_at: str
    lon: int
    lat: int
