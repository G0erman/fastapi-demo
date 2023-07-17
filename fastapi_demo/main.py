"""Original Example from https://fastapi.tiangolo.com/."""
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Returns a dictionary."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, query: Union[str, None] = None):
    """Automatic valiation from type integer"""
    return {"item_id": item_id, "query": query}
