# Main Service API for Items
from typing import Optional

from fastapi import FastAPI
from .schema import Item
from .db import SessionLocal, db_eng
from . import item_handling, db_models, schema



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