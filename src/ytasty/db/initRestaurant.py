from ytasty.modules.restaurants.model import Restaurant


def seed_restaurants(db):
    restaurants = [
        {
            "name": "Ytasty Crousty Aix",
            "city": "Aix-en-Provence",
            "address": "Adresse à définir",
            "is_open": True,
            "opening_hours": "À définir",
            "contact": "À définir",
        },
        {
            "name": "Ytasty Crousty Lyon",
            "city": "Lyon",
            "address": "Adresse à définir",
            "is_open": True,
            "opening_hours": "À définir",
            "contact": "À définir",
        },
        {
            "name": "Ytasty Crousty Paris",
            "city": "Paris",
            "address": "Adresse à définir",
            "is_open": True,
            "opening_hours": "À définir",
            "contact": "À définir",
        },
    ]

    for restaurant_data in restaurants:
        restaurant = db.query(Restaurant).filter(
            Restaurant.name == restaurant_data["name"]
        ).first()

        if restaurant is None:
            new_restaurant = Restaurant(**restaurant_data)
            db.add(new_restaurant)

    db.commit()