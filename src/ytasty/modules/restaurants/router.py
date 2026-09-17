from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ytasty.db.database import get_db
from ytasty.modules.restaurants import service


router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)


@router.get("")
def get_restaurants(db: Session = Depends(get_db)):
    return service.get_restaurants(db)
