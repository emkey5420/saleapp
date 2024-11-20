from sqlalchemy import Column, Integer, String, Float
from app import db, app

class Category(db.Model):

    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String )