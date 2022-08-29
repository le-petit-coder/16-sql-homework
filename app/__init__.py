from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import data


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['RESTX_JSON']={'ensure_ascii':False,'indent':4}

    with app.app_context():
        db.init_app(app)
        from . import views
        db.create_all()
        from . import utils
        utils.load_users('./data/users.json')
        utils.load_orders('./data/orders.json')
        utils.load_offers('./data/offers.json')

    return app