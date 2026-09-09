from pydantic import BaseModel, EmailStr


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr


class OrderCreate(BaseModel):
    restaurant_id: int
    items: list[OrderItemCreate]
    pickup_mode: str
    customer: CustomerCreate


class OrderStatusUpdate(BaseModel):
    status: str
