from flask import Blueprint, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from .weather import get_lat_lon, get_current_weather, api_key

views = Blueprint('views', __name__)

class city_name(FlaskForm):
  name = StringField('City Name: ', validators=[DataRequired()])
  country_name = StringField('Country Name: ', validators=[DataRequired()])
  submit = SubmitField('Submit')

@views.route('/')
def home():
  return render_template('index.html')

@views.route('/weather', methods=["POST", "GET"])
def weather():
  name = None
  country_name = None
  form = city_name()

  if request.method == "POST":
    if form.validate_on_submit():
      name = form.name.data
      form.name.data = ''
      country_name = form.country_name.data
      form.country_name.data = ''
      
      lat, lon = get_lat_lon(name, 'ON', country_name, api_key)
      data = get_current_weather(lat, lon, api_key)
      
      return render_template("weather.html", name=name, form=form, data=data)

  return render_template("weather.html", form=form)
