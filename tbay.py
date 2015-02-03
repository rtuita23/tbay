from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import  datetime
from sqlalchemy import Column, Integer, String, DateTime, Float

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
print 'after class item'
class User(Base):
    __tablename__="name"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
print 'after class user'

class Bid(Base):
    __tablename__="bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
print 'after bid'
    
Base.metadata.create_all(engine)

print 'last line'





