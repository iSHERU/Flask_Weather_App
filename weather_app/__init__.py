from flask import Flask
from os import path
from .models import db

DB_NAME = "weather.db"


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secret_key'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)

  with app.app_context():
    db.create_all()


  from .views import views

  app.register_blueprint(views, url_prefix='/')

  return app



def create_database(app):
  if not path.exists('website/' + DB_NAME):
    db.create_all(app=app)