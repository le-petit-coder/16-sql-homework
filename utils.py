import json


def get_all_users():
    with open('users.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all_orders():
    with open('orders.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all_offers():
    with open('offers.json', 'r', encoding='utf-8') as file:
        return json.load(file)

