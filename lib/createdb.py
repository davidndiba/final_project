from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import User, Car, Seller, Buyer  # Import your models here

DATABASE_URL = "sqlite:///finalp.db"  
engine = create_engine(DATABASE_URL)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

print("All tables created successfully.")
