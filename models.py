from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    description: str
    quantity: int