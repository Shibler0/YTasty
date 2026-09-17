from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ytasty.db.database import get_db
from ytasty.modules.products import service


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