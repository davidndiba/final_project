from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from models import User, Car, Seller, Buyer, Transaction
from faker import Faker

DATABASE_URL = "sqlite:///finalp.db"  
engine = create_engine(DATABASE_URL, poolclass=QueuePool)
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

def seed_data():
    
    users = []
    for _ in range(4):
        user = User(
            user_name=fake.user_name(),
            email=fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number=fake.random_int(min=1000000000, max=9999999999),
            address=fake.address(),
        )
        users.append(user)

    session.add_all(users)
    session.commit()

    
    sellers = []
    for user_id in range(1, 4):
        seller = Seller(
            user_id=user_id,
            name=fake.name(),
            address=fake.address(),
        )
        sellers.append(seller)

    session.add_all(sellers)
    session.commit()

    
    buyers = []
    for user_id in range(1, 4):
        buyer = Buyer(
            user_id=user_id,
            name=fake.name(),
            address=fake.address(),
        )
        buyers.append(buyer)

    session.add_all(buyers)
    session.commit()

    
    cars = []
    for seller_id in range(1, 4):
        for _ in range(3):
            car = Car(
                make=fake.company(),
                model=fake.random_element(elements=("Sedan", "SUV", "Truck", "Convertible")),
                year=fake.random_int(min=2000, max=2023),
                price=fake.random_int(min=5000, max=50000),
                seller_id=seller_id,
            )
            cars.append(car)

    session.add_all(cars)
    session.commit()

    
    transactions = []
    for buyer_id in range(1, 4):
        for _ in range(2):
            transaction = Transaction(
                transaction_date=fake.date_time_this_decade(),
                transaction_amount=fake.random_int(min=100, max=5000),
                buyer_id=buyer_id,
            )
            transactions.append(transaction)

    session.add_all(transactions)
    session.commit()

if __name__ == "__main__":
    seed_data()
