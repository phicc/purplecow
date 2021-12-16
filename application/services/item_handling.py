from typing import List
from sqlalchemy.orm import Session
from . import db_models, schema

def get_items(db: Session):
    # Gather all items from DB
    # Considering accepting pagination params
    return db.query(db_models.Item).all()

def set_items(db: Session, items: List[schema.ItemCreate]):
    # Set items in DB
    def toItem(passedItem):
        return db_models.Item(id=passedItem.id, name=passedItem.name)
    new_items = map(toItem, items)
    db.bulk_save_objects(new_items)
    db.commit()
    return new_items

def set_item(db: Session, item: schema.ItemCreate):
    # Set items in DB
    new_item = db_models.Item(id=item.id, name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def delete_items(db: Session):
    # Delete all items in DB
    return db.delete()