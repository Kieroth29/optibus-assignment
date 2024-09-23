from pydantic import BaseModel


class Trip(BaseModel):
    trip_id: int
    route_number: int
    origin_stop_id: str
    destination_stop_id: str
    departure_time: str
    arrival_time: str