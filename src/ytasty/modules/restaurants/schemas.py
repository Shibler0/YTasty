from pydantic import BaseModel


class RestaurantUpdate(BaseModel):
    address: str | None = None
    contact: str | None = None


class RestaurantAvailabilityUpdate(BaseModel):
    is_open: bool
