from ytasty.common.errors import NotFoundError
from ytasty.modules.restaurants import repository

def get_restaurants(db):
    return repository.get_restaurants(db)


def get_restaurant_by_id(db, restaurant_id: int):
    restaurant = repository.get_restaurant_by_id(
        db,
        restaurant_id,
    )

    if restaurant is None:
        raise NotFoundError("Restaurant introuvable")

    return restaurant