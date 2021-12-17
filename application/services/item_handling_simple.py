# Simple data handling functionality expecting to update a list of dicts
from typing import List
from . import db_models, schema

def get_item(db: List, id: str):
    id_item = {}
    for item in db:
        if item.id == id:
            id_item = item
            break
    return id_item

def get_items(db: List):
    # Gather all items from DB
    # Considering accepting pagination params
    return db

def set_items(db: List, items: List[schema.Item]):
    # Set items in DB
    db.extend(items)
    return items

def set_item(db: List, item: schema.Item):
    # Set items in DB
    db.append(item)
    return item

def delete_items(db: List):
    # Delete all items in DB
    return db.clear()