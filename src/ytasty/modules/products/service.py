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