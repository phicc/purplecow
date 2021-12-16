# Main Service API for Items
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class ItemModel(BaseModel):
    id: str
    name: str


app = FastAPI()

@app.get("/items/{id}")
def get_single_item(
    id: str
):
    # Retrieve the single item by id
    return

@app.get("/items")
def get_items():
    # Retrieve all items
    return

@app.put('/items')
def set_items():
    # Set the items
    return

@app.delete('/items')
def delete_items():
    # Delete the items
    return