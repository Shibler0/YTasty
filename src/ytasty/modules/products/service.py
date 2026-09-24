from ytasty.common.errors import NotFoundError
from ytasty.modules.products import repository
from ytasty.common.errors import ForbiddenError
from ytasty.modules.restaurants import service as restaurants_service


def get_products(
    db,
    category=None,
    q=None,
    restaurant_id=None,
    is_available=None,
):
    return repository.get_products(
        db,
        category,
        q,
        restaurant_id,
        is_available,
    )


def get_product(db, product_id: int):
    product = repository.get_product(db, product_id)

    if product is None:
        raise NotFoundError("Produit introuvable")

    return product

def create_product(db, data, current_user):
    if current_user.role == "staff":
        if current_user.restaurant_id != data.restaurant_id:
            raise ForbiddenError("Ce restaurant n'est pas le vôtre")
    elif current_user.role != "admin":
        raise ForbiddenError("Vous ne pouvez pas créer de produit")

    restaurants_service.get_restaurant_by_id(db, data.restaurant_id)

    return repository.create_product(db, data)