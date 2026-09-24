from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ytasty.db.database import get_db
from ytasty.modules.products import service
from ytasty.modules.auth.dependencies import get_current_user
from ytasty.modules.products.schemas import ProductCreate, ProductResponse
from ytasty.modules.users.model import User


router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.get("")
def get_products(
    category: str | None = None,
    q: str | None = None,
    restaurant_id: int | None = None,
    is_available: bool | None = None,
    db: Session = Depends(get_db),
):
    return service.get_products(
        db,
        category,
        q,
        restaurant_id,
        is_available,
    )


@router.get("/{product_id}")
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    return service.get_product(db, product_id)

@router.post("", response_model=ProductResponse, status_code=201)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return service.create_product(db, data, current_user)