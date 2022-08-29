import json
from . import models, db


def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_users(filename):
    users = load_data(filename)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)
    db.session.commit()


def load_orders(filename):
    orders = load_data(filename)

    for order in orders:
        new_order = models.Order(**order)
        db.session.add(new_order)
    db.session.commit()


def load_offers(filename):
    offers = load_data(filename)

    for offer in offers:
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)
    db.session.commit()



