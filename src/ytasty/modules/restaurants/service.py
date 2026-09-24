from ytasty.common.errors import NotFoundError, ForbiddenError
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

def update_availability(db, restaurant_id: int, is_open: bool, current_user):
    if current_user.role != "admin":
        raise ForbiddenError("Seul un administrateur peut modifier la disponibilité")

    restaurant = get_restaurant_by_id(db, restaurant_id)

    return repository.update_availability(db, restaurant, is_open)