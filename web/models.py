# models.py
from app import db

from sqlalchemy import String, Integer, Column
class Post(db.Model):

    __tablename__ = 'solutions'
    
    n = Column(Integer, primary_key=True)
    sol = Column(String)

    
        
