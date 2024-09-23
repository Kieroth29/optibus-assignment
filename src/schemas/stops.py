from pydantic import BaseModel


class Stop(BaseModel):
    stop_id: str
    stop_name: str
    latitude: float
    longitude: float
    is_depot: bool