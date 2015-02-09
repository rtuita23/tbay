'''
    MODELS RELATIONSHIPS
    
    users should be able to auction multiple items
    1 user to many items relationship
    
    users should be able to bid on multiple items
    many users to many items relationship
    
    multiple users should be able to place a bid on an item
    1 item to many users relationship
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import  datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

print '1'

class User(Base):
    __tablename__='name'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    items = relationship("Item", backref="nameitem")
    bids = relationship('Bid', backref="namebid")

print '2'

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('name.id'), nullable=False)

print '3'    

class Bid(Base):
    __tablename__="bid"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    
    user_id = Column(Integer, ForeignKey('name.id'), nullable=False)
    items_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    
print '4'
    
Base.metadata.create_all(engine)

print '5'

#u1 = User(username = 'Ivi', password = 'ivi')
#mateo = User(username = 'Teo', password = 'teo')
#baseball = Item(name='baseball', description = 'brown ball', start_time = datetime.utcnow())
#mateo.items = [baseball]
#ivi_bid = Bid(price=12.0, user_id = 3, items_id = 1)
#kaho_bid = Bid(price=7.0, user_id = 2, items_id = 1)
#fia_bid = Bid(price=8.0, user_id = 1, items_id = 1)
#session.add_all([fia_bid, ivi_bid, kaho_bid])
session.query(Bid.user_id).order_by(Bid.price).all()
session.commit()