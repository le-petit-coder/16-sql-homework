import prettytable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import get_all_users,get_all_offers, get_all_orders
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(100))
    phone = db.Column(db.String)
    order = relationship("Order")
    offer = relationship("Offer")


class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(250))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String(150))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("offers.id"))

    customer = relationship("User")
    executor = relationship("Offer")


class Offer(db.Model):
    __tablename__ = 'offers'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    order = relationship("Order")
    executor = relationship("User")

db.create_all()

users_dict = [User(**meaning) for meaning in get_all_users()]
orders_dict = [User(**meaning) for meaning in get_all_orders()]
offers_dict = [User(**meaning) for meaning in get_all_offers()]

with db.session.begin():
    db.session.add_all(users_dict)
    db.session.add_all(orders_dict)
    db.session.add_all(offers_dict)

db.session.commit()

if __name__ == '__main__':
    app.run()


