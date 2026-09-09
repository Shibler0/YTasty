from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    image: str
    description: str
    category: str
    price: float
    is_available: bool
    restaurant_id: int
    ingredients: list[str]


class ProductAvailabilityUpdate(BaseModel):
    is_available: bool
