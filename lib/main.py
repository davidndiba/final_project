import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Car

DATABASE_URL = "sqlite:///finalp.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--user_name', prompt='Enter user_name', help='User Name')
@click.option('--email', prompt='Enter email', help='Email')
@click.option('--first_name', prompt='Enter first_name', help='First Name')
@click.option('--last_name', prompt='Enter last_name', help='Last Name')
@click.option('--phone_number', prompt='Enter phone_number', help='Phone Number')
@click.option('--address', prompt='Enter address', help='Address')
def create_user(user_name, email, first_name, last_name, phone_number, address):
    new_user = User(
        user_name=user_name,
        email=email,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        address=address
    )
    session.add(new_user)
    session.commit()
    print(f"User '{user_name}' added successfully!")

@cli.command()
@click.argument('user_id', type=int)
def delete_user(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} deleted successfully!")
    else:
        print(f"User with ID {user_id} not found.")

@cli.command()
@click.option('--make', prompt='Enter car make', help='Car Make')
@click.option('--model', prompt='Enter car model', help='Car Model')
@click.option('--year', prompt='Enter car year', help='Car Year')
@click.option('--price', prompt='Enter car price', help='Car Price')
@click.option('--seller_id', prompt='Enter seller_id', help='Seller ID')
def create_car(make, model, year, price, seller_id):
    new_car = Car(
        make=make,
        model=model,
        year=year,
        price=price,
        seller_id=seller_id
    )
    session.add(new_car)
    session.commit()
    print(f"Car added successfully!")

@cli.command()
@click.argument('car_id', type=int)
def delete_car(car_id):
    car = session.query(Car).filter_by(id=car_id).first()
    if car:
        session.delete(car)
        session.commit()
        print(f"Car with ID {car_id} deleted successfully!")
    else:
        print(f"Car with ID {car_id} not found.")

if __name__ == "__main__":
    cli()
