from flask import Flask, render_template, request
import requests
from requests import Response
import os
from dotenv import load_dotenv
import json

app = Flask(__name__)


def configure():
    load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html')


def get_weather(city):
    api_key = os.getenv("API_KEY")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = json.loads(response.text)

    if 'weather' in data and 'temp' in data['main']:
        temperature = round(data['main']['temp'] - 273.15, 2)
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
    else:
        temperature = 'N/A'
        humidity = 'N/A'
        wind_speed = 'N/A'
    
    if 'weather' in data and len(data['weather']) > 0:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
    else:
        description = 'N/A'
        icon = 'N/A'

    weather_data = {
        'city': city,
        'temperature': temperature,
        'description': description.title(),
        'icon': icon,
        'humidity': humidity,
        'wind_speed': wind_speed
    }

    return weather_data


if __name__ == '__main__':
    app.run(debug=True)



###################### ---> TRIAL <--- ######################
# def fetch_weather_data(city):
#     api_key = os.getenv("API_KEY")
#     base_url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#     params = {
#         "q" : city,
#         "appid" : api_key,
#         "units" : "metric"   
#     }
    
#     try:
#         response = requests.get(base_url.format(city=city), params=params)
#         response.raise_for_status()
#         data = response.json()
#         return data
#     except response.exceptions.RequestException as e:
#         print("Error occured:", e)
#         return None 
    
# def display_weather_data(weather_data):
#     if weather_data is None:
#         print("Unable to fetch weather data")
#     else:
#         print(weather_data)
    
# @app.route('/')
# def index():
#      return render_template("index.html")    
        
  
  
# @app.route('/search', methods=['POST', 'GET'])
# def search():
#     city_name = request.form['city']
#     weather_data = fetch_weather_data(city_name)
#     display_weather_data(weather_data)
#     return render_template('index.html', weather_data=weather_data) 

# if __name__=="__main__":
#     configure()
#     app.run(debug=True)
##################### ----> END OF TRIAL <----- #########################