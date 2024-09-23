from datetime import time
from typing import List

from pydantic import BaseModel

from schemas.duties import Duty
from schemas.stops import Stop
from schemas.trips import Trip
from schemas.vehicles import Vehicle


class Schedule(BaseModel):
    stops: List[Stop]
    trips: List[Trip]
    vehicles: List[Vehicle]
    duties: List[Duty]


class Break(BaseModel):
    start_time: time
    duration: int
    stop_name: str


class Report(BaseModel):
    start_time: str
    end_time: str
    start_stop_description: str
    end_stop_description: str
    breaks: List[Break]
