
from flask import Flask, render_template,request
from datetime import datetime
import requests
import os

app = Flask(__name__)
url = "https://api.open-meteo.com/v1/forecast"
url_geo = "https://geocoding-api.open-meteo.com/v1/search"
def get_coordinates(city_name):
    
    params = {
            "name": city_name,
            "count": 1  # just get the top match
    }
    try:
        response = requests.get(url_geo, params=params,timeout = 10)
        data = response.json()
    except requests.exceptions.RequestException:
        return None
    if "results" not in data:
        return None # city not found

    result = data["results"][0]
    matched_name = result["name"]
    latitude = result["latitude"]
    longitude = result["longitude"]
    return latitude, longitude,matched_name
def get_weather(lat,long):
    params = {
           'latitude' : lat,
           'longitude' : long,
           'current' : 'temperature_2m,weather_code',
           'timezone' : 'auto'
      }
    try:
        response = requests.get(url,params = params,timeout = 10)
        data = response.json()
    except requests.exceptions.RequestException:
        return None,None
    if 'current' not in data :
      return None,None
    return data['current']['temperature_2m'],data['current']['weather_code']
def get_description(code):
    mapping = {
        0: ("Clear sky", "clear-day"),
        1: ("Mainly clear", "clear-day"),
        2: ("Partly cloudy", "partly-cloudy-day"),
        3: ("Overcast", "overcast"),
        45: ("Fog", "fog"),
        48: ("Fog", "fog"),
        51: ("Light drizzle", "drizzle"),
        53: ("Drizzle", "drizzle"),
        55: ("Heavy drizzle", "drizzle"),
        61: ("Light rain", "rain"),
        63: ("Rain", "rain"),
        65: ("Heavy rain", "rain"),
        71: ("Light snow", "snow"),
        73: ("Snow", "snow"),
        75: ("Heavy snow", "snow"),
        80: ("Rain showers", "rain"),
        81: ("Rain showers", "rain"),
        82: ("Violent rain showers", "rain"),
        95: ("Thunderstorm", "thunderstorms"),
        96: ("Thunderstorm with hail", "thunderstorms-hail"),
        99: ("Thunderstorm with hail", "thunderstorms-hail"),
    }
    return mapping.get(code,  ("Unknown", "clear-day"))
@app.route('/',methods=['GET', 'POST']) # this decorator create the home route
def index():
    temp = None
    name = None
    time = None
    description = None 
    error = None
    icon = None
    if(request.method == 'POST'):
        city = request.form.get('content', '').strip()
        if city:
          coordinates = get_coordinates(city)
          if coordinates :
                latitude,longitude,name = coordinates
                time = datetime.now().strftime("%I:%M %p")
                temp,weather_code= get_weather(latitude,longitude)
                if(temp is None or weather_code is None):
                    error = "Weather service is unavailable for a moment please try again after sometime"
                else:
                   description,icon= get_description(weather_code)
          else:
            error = f"couldn't find {city},please check the spelling and try again"
        else:
            error = "please enter a city"
         
           
    return render_template('index.html',temp = temp,city = name,time = time,description = description,error = error,icon = icon )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_DEBUG", "False") == "True"
    app.run(debug= debug_mode, host='0.0.0.0', port=port)
    