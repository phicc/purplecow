from sqlalchemy import String, Column
from .db import DBBase

class Item(DBBase):
    __tablename__ = "items"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)