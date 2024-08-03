from flask import Flask
from .models import db

DB_NAME = "weather.db"


def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secret_key'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  with app.app_context():
    db.init_app(app)
    db.create_all()
  db.init_app(app)

  from .views import views

  app.register_blueprint(views, url_prefix='/')

  return app
