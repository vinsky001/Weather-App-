from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)


def configure():
    load_dotenv()

def fetch_weather_data(city):
    api_key = os.getenv("API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : "metrics"   
    }
    
    try:
        response = response.get(base_url, params=params)
        response = response.raise_for_status()
        data = response.Json()
        return data
    except response.exceptions.RequestException as e:
        print("Error occured", e)
        return None 
    
def display_weather_data(weather_data):
    if weather_data is None:
        print("Unable to fetch weather data")
        return
  
  
@app.route('/search', methods=['POST'])
def search():
    city_name = request.form["city"]
    weather_data = fetch_weather_data(city.name)
    display_weather_data(weather_data)
    return render_template(app.index.html, weather_data=weather_data) 

if __name__=="__main__":
    app.run(debug=True)         