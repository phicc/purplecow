# Main Service API for Items
from typing import List

from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm.session import Session
from .schema import Item
from .db import SessionLocal, db_eng
from . import item_handling, db_models, schema
from application.services import db

db_models.DBBase.metadata.create_all(bind=db_eng)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/{id}")
def get_single_item(
    id: str
):
    # Retrieve the single item by id
    return

@app.get("/items", response_model=List[schema.Item])
def get_items(db: Session = Depends(get_db)):
    # Retrieve all items
    return item_handling.get_items(db=db)

@app.post('/items', response_model=schema.Item)
def set_items(items: List[schema.ItemCreate], db: Session = Depends(get_db)):
    # Set the items
    def toItem(passedItem):
        return db_models.Item(id=passedItem.id, name=passedItem.name)
    new_items = map(toItem, items)
    return item_handling.set_items(db=db, items=new_items)

@app.delete('/items')
def delete_items(db: Session = Depends(get_db)):
    # Delete the items
    return item_handling.delete_items(db=db)