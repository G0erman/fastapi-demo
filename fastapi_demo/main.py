"""Original Example from https://fastapi.tiangolo.com/."""
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    """Define the model of the input."""

    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    """Returns a dictionary."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Union[str, None] = None):
    """Automatic valiation from type integer"""
    return {"item_id": item_id, "query": query}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """The item to updated must have the BaseModel."""
    return {"item_name": item.name, "item_id": item_id}
