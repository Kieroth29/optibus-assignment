from __future__ import annotations
from typing import List, Optional

from pydantic import BaseModel


class Duty(BaseModel):
    duty_id: int
    duty_events: List[DutyEvent]


class DutyEvent(BaseModel):
    duty_event_sequence: int
    duty_event_type: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    origin_stop_id: Optional[str] = None
    destination_stop_id: Optional[str] = None
    vehicle_event_sequence: Optional[int] = None
    vehicle_id: Optional[int] = None