from fastapi import APIRouter


router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"],
)

# Les endpoints du module restaurants seront ajoutes ici.
