from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String)
    quantity: Mapped[int] = mapped_column(Integer)
