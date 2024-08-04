from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

views = Blueprint('views', __name__)

class city_name(FlaskForm):
  name = StringField('City Name: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

@views.route('/')
def home():
  return render_template('index.html')


@views.route('/weather', methods=["POST", "GET"])
def weather():
  name = None
  form = city_name()

  if request.method == "POST":
    if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''

      return render_template("weather.html", name=name, form=form)
  return render_template("weather.html", form=form)

def check_weather(city):
  # TODO: Implement this function

  return "Weather data for {} is coming soon!".format(city)
