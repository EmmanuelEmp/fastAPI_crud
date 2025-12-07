from fastapi import FastAPI , Depends, HTTPException
from models import ProductSchema
import database_models
from database import session, engine
import crud

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
@app.post("/products/", response_model=ProductSchema)
def create_product(product: ProductSchema, db=Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/", response_model=list[ProductSchema])
def read_products(db=Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=ProductSchema)
def read_product(product_id: int, db=Depends(get_db)):
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=ProductSchema)
def update_product(product_id: int, product: ProductSchema, db=Depends(get_db)):
    db_product = crud.update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{product_id}", response_model=ProductSchema)
def delete_product(product_id: int, db=Depends(get_db)):
    db_product = crud.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

