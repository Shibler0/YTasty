from ytasty.modules.restaurants.model import Restaurant


def get_restaurants(db):
    return db.query(Restaurant).all()
