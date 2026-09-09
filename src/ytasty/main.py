from fastapi import FastAPI
from ytasty.db.base import Base
from ytasty.db.database import engine
from ytasty.modules.auth.router import router as auth_router
from ytasty.modules.orders.model import Order, OrderItem
from ytasty.modules.orders.router import router as orders_router
from ytasty.modules.products.model import Product
from ytasty.modules.products.router import router as products_router
from ytasty.modules.restaurants.model import Restaurant
from ytasty.modules.restaurants.router import router as restaurants_router
from ytasty.modules.users.model import User
from ytasty.modules.users.router import router as users_router


MODELS = [
    Restaurant,
    User,
    Product,
    Order,
    OrderItem,
]

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ytasty Crousty API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(restaurants_router)
app.include_router(products_router)
app.include_router(orders_router)


@app.get("/health")
def health():
    return {"status": "ok"}
