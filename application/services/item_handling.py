from sqlalchemy.orm import Session
from . import db_models, schema

def get_items(db: Session):
    # Gather all items from DB
    # Considering accepting pagination params
    return db.query(db_models.Item).all()

def set_items(db: Session, item: schema.ItemCreate):
    # Set items in DB
    new_item = db_models.Item(id=item.id, name=item.name)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def delete_items(db: Session):
    # Delete all items in DB
    return db.delete()