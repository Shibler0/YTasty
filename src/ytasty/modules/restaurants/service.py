from ytasty.modules.restaurants import repository

def get_restaurants(db):
    return repository.get_restaurants(db)