from pydantic import BaseModel
from typing import List
from datetime import datetime
from .order_item import OrderItemCreate, OrderItemResponse


class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    total_amount: float
    status: str
    created_at: datetime
    updated_at: datetime
    order_items: List[OrderItemResponse]

    class Config:
        from_attributes = True
