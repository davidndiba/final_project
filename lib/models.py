from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///finalp.db"  

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

metadata = MetaData()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    user_name = Column(String())  
    email = Column(String(), unique=True)  
    first_name = Column(String())  
    last_name = Column(String())  
    phone_number = Column(Integer())  
    address = Column(String())  

    sellers = relationship("Seller", back_populates="user")
    buyers = relationship("Buyer", back_populates="user")


class Buyer(Base):
    __tablename__ = 'buyers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())  
    address = Column(String())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="buyers")
    transactions = relationship("Transaction", back_populates="buyer")


class Seller(Base):
    __tablename__ = 'sellers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())  
    address = Column(String())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="sellers")
    cars = relationship("Car", back_populates="seller")


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer(), primary_key=True)
    make = Column(String())
    model = Column(String())
    year = Column(Integer())
    price = Column(Integer())
    seller_id = Column(Integer, ForeignKey("sellers.id"))

    seller = relationship("Seller", back_populates="cars")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer(), primary_key=True)
    transaction_date = Column(Integer())
    transaction_amount = Column(Integer())   
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    
    buyer = relationship("Buyer", back_populates="transactions")

Base.metadata.create_all(bind=engine)
