import requests
import json
from dataclasses import dataclass

with open('../Flask_Weather_App/creds.json') as cred:
    data = json.load(cred)

api_key = data['API_KEY']['API_Key']

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temp_min: float
    temp_max: float

def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')

    return lat, lon

def get_current_weather(lat, lon, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}').json()
    
    data = WeatherData (
        main = resp.get('weather')[0].get('main'),
        description = resp.get('weather')[0].get('description'),
        icon = resp.get('weather')[0].get('icon'),
        temp_min = resp.get('main').get('temp_min'),
        temp_max = resp.get('main').get('temp_max')
    )
    
    return data