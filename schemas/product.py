from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    sku: str
    price: float
    quantity: int


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    price: float
    quantity: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
