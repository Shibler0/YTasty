from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

# L'endpoint POST /auth/login sera ajoute ici.
