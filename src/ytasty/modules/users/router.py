from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# Les endpoints du module users seront ajoutes ici.
