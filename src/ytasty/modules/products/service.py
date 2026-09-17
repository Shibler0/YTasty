from ytasty.common.errors import NotFoundError
from ytasty.modules.products import repository


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