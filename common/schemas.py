from enum import Enum
from typing import Literal

from pydantic import BaseModel


class Status(Enum):
    OK: str = "OK"
    ERROR: str = "ERROR"


class HttpResponse(BaseModel):
    status: Literal[Status.OK, Status.ERROR] = Status.OK
    data: dict = {}


class Location(Enum):
    LIVING_ROOM = 1


class SensorInput(BaseModel):
    activated_at: str
    lon: int
    lat: int
    location: int

    def to_dict(self) -> dict:
        return {
            "activated_at": self.activated_at,
            "lat": self.lat,
            "lon": self.lon,
            "location": Location(self.location).name,
        }


class HouseToy(BaseModel):
    toy_name: str


class HouseToys(BaseModel):
    toys: list

    def __str__(self) -> str:
        return ", ".join([toy.get("name") for toy in self.toys])
