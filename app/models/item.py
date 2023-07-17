"""Data Models used in app"""
from typing import Union

from pydantic import BaseModel


class Item(BaseModel):
    """Define the model of the input."""

    name: str
    price: float
    is_offer: Union[bool, None] = None
