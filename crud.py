from models import ProductSchema
from database_models import Product
from database import session, engine
from sqlalchemy.orm import Session


def create_product(db: Session, product: ProductSchema):
    new_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def get_products(db: Session):
    return db.query(Product).all()

def get_product(db: Session, product_id: int):
    return db.query(Product).filter(product_id == Product.id).first()

def update_product(db: Session, product_id: int, product: ProductSchema):
    existing_product = db.query(Product).filter(Product.id == product_id).first()
    if existing_product:
        existing_product.name = product.name
        existing_product.price = product.price
        existing_product.description = product.description
        existing_product.quantity = product.quantity
        db.commit()
        db.refresh(existing_product)
    return existing_product

def delete_product(db:Session, product_id: int, product: ProductSchema):
    del_product = db.query(Product).filter(Product.id == product_id).first()
    if del_product:
        db.delete(del_product)
        db.commit()
    return del_product
    