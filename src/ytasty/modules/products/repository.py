from ytasty.modules.products.model import Product

from ytasty.modules.products.model import Product


def get_product(db, product_id: int):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()

def get_products(
    db,
    category=None,
    q=None,
    restaurant_id=None,
    is_available=None,
):
    query = db.query(Product)

    if category is not None:
        query = query.filter(Product.category == category)

    if q is not None:
        query = query.filter(Product.name.ilike(f"%{q}%"))

    if restaurant_id is not None:
        query = query.filter(
            Product.restaurant_id == restaurant_id
        )

    if is_available is not None:
        query = query.filter(
            Product.is_available == is_available
        )

    return query.all()