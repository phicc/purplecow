# Main Service API for Items
from typing import List

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from .schema import Item
from . import item_handling_simple, db_models, schema

app = FastAPI()
# When initializing the APP also create our storage
simple_db = []

def get_db_simple():
    return simple_db

@app.get("/items/{id}")
def get_single_item(
    id: str, db: Session = Depends(get_db_simple)
):
    # Retrieve the single item by id
    return item_handling_simple.get_item(db=db, id=id)

@app.get("/items")
def get_items(db: Session = Depends(get_db_simple)):
    # Retrieve all items
    return item_handling_simple.get_items(db=db)

@app.post('/items')
def set_items(items: List[schema.Item], db: Session = Depends(get_db_simple)):
    # Set the items
    return item_handling_simple.set_items(db=db, items=items)

@app.delete('/items')
def delete_items(db: Session = Depends(get_db_simple)):
    # Delete the items
    return item_handling_simple.delete_items(db=db)