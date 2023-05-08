from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, conint, validator, conlist


class Size(Enum):
    small = "small"
    medium = "medium"
    big = "big"


class StatusEnum(Enum):
    created = "created"
    paid = "paid"
    progress = "progress"
    cancelled = "cancelled"
    dispatched = "dispatched"
    delivered = "delivered"

class UnitSchema(BaseModel):
    codUnit: int
    name:str
 
class CreateUnitSchema(BaseModel):
    units:List[UnitSchema]
    # conlist(UnitSchema, min_items=1)

class GetRequestTypeSchema(CreateUnitSchema):
    codRequestType: int
    requestType: str
    # baseUnitID: int = 1

class GetRequestsTypesSchema(BaseModel):
    requestTypes:List[GetRequestTypeSchema]

# class OrderItemSchema(BaseModel):

#     product: str
#     size: Size
#     quantity: Optional[conint(ge=1, strict=True)] = 1

#     @validator("quantity")
#     def quantity_non_nullable(cls, value):
#         assert value is not None, "quantity may not be None"
#         return value


# class CreateOrderSchema(BaseModel):
#     order: conlist(OrderItemSchema, min_items=1)


# class GetOrderSchema(CreateOrderSchema):
#     id: UUID
#     created: datetime
#     status: StatusEnum


# class GetOrdersSchema(BaseModel):
#     orders: List[GetOrderSchema]
