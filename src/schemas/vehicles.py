from __future__ import annotations
from typing import List, Optional

from pydantic import BaseModel


class Vehicle(BaseModel):
    vehicle_id: int
    vehicle_events: List[VehicleEvent]

class VehicleEvent(BaseModel):
    vehicle_event_sequence: int
    vehicle_event_type: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    origin_stop_id: Optional[str] = None
    destination_stop_id: Optional[str] = None
    duty_id: int
    trip_id: Optional[int] = None