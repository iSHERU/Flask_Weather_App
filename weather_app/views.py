from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)


@views.route('/')
def home():
  return render_template('index.html')


@views.route('/weather', methods=["POST", "GET"])
def weather():
  if request.method == "POST":
    city = request.form.get("city")
    weather_data = check_weather(city)

    return render_template('weather.html', weather_data=weather_data)
  return render_template('weather.html')


def check_weather(city):
  # TODO: Implement this function

  return "Weather data for {} is coming soon!".format(city)
