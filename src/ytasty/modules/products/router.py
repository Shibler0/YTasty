from fastapi import APIRouter


router = APIRouter(
    prefix="/products",
    tags=["products"],
)

# Les endpoints du module products seront ajoutes ici.
