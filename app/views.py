from app import models, db
from flask import jsonify, current_app as app, request
import json


@app.route("/users", methods=['GET', 'POST'])
def page_users():
    if request.method == 'GET':
        result = []
        for user in models.User.query.all():
            result.append(user.change_to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        data_user = json.loads(request.data)
        new_user = models.User(**data_user)
        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in models.User.query.all():
            result.append(user.change_to_dict())
        return result


@app.route("/users/<int:uid>", methods=['GET', 'POST', 'DELETE'])
def one_user(uid):
    if request.method == 'GET':
        user = models.User.query.get(uid)
        return jsonify(user.change_to_dict())
    if request.method == 'PUT':
        user_data = request.json() #
        user = models.User.query.get(uid)
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.age = user_data['age']
        user.email = user_data['email']
        user.role = user_data['role']
        user.phone = user_data['phone']

        db.session.add(user)
        db.session.commit()

        user = models.User.query.get(uid)
        return user
    if request.method == 'DELETE':
        user = models.User.query.get(uid)
        db.session.delete(user)
        db.session.commit()

        return "", 200


@app.route("/orders", methods=['GET', 'POST'])
def page_orders():
    if request.method == 'GET':
        result = []
        for order in models.Order.query.all():
            result.append(order.change_to_dict())
        return jsonify(result), {'Content-type': 'application/json; charset=utf-8'}
    elif request.method == 'POST':
        data_order = json.loads(request.data)
        new_order = models.User(**data_order)
        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in models.Order.query.all():
            result.append(order.change_to_dict())
        return result


@app.route("/orders/<int:uid>", methods=['GET', 'POST', 'DELETE'])
def one_order(uid):
    if request.method == 'GET':
        order = models.Order.query.get(uid)
        return jsonify(order.change_to_dict())
    if request.method == 'PUT':
        order_data = request.json() #
        order = models.Order.query.get(uid)
        order.name = order_data['name']
        order.description = order_data['description']
        order.start_date = order_data['start_date']
        order.end_date = order_data['end_date']
        order.address = order_data['address']
        order.price = order_data['price']

        db.session.add(order)
        db.session.commit()

        user = models.Order.query.get(uid)
        return user
    if request.method == 'DELETE':
        order = models.Order.query.get(uid)
        db.session.delete(order)
        db.session.commit()

        return "", 200


@app.route("/offers", methods=['GET', 'POST'])
def page_offers():
    if request.method == 'GET':
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.change_to_dict())
        return jsonify(result), 200
    elif request.method == 'POST':
        offer_data = json.loads(request.data)
        new_offer = models.User(**offer_data)
        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in models.Offer.query.all():
            result.append(offer.change_to_dict())
        return result


@app.route("/offers/<int:uid>", methods=['GET', 'POST', 'DELETE'])
def one_offer(uid):
    if request.method == 'GET':
        offer = models.Offer.query.get(uid)
        return jsonify(offer.change_to_dict())
    if request.method == 'PUT':
        offer_data = request.json() #
        offer = models.Offer.query.get(uid)
        offer.order_id = offer_data['order_id']
        offer.executor_id = offer_data['executor_id']

        db.session.add(offer)
        db.session.commit()

        offer = models.Offer.query.get(uid)
        return offer
    if request.method == 'DELETE':
        offer = models.Offer.query.get(uid)
        db.session.delete(offer)
        db.session.commit()

        return "", 200