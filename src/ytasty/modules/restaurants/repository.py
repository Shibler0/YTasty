from ytasty.modules.restaurants.model import Restaurant


def get_restaurants(db):
    return db.query(Restaurant).all()


def get_restaurant_by_id(db, restaurant_id: int):
    return db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()