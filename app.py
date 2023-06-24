# Import necessary modules
from flask import Flask, render_template, request
import requests
from requests import Response
import os
from dotenv import load_dotenv
import json

# Create a Flask application instance
app = Flask(__name__)


# Load environment variables
def configure():
    load_dotenv()


# Define route for root URL with GET and POST methods
@app.route("/", methods=["GET", "POST"])
def index():
    # Check if request method is POST
    if request.method == "POST":
        # Retrieve value of 'city' form field submitted by user
        city = request.form["city"]

        # Call get_weather() function to retrieve weather data
        weather_data = get_weather(city)

        # Render 'index.html' template with weather data
        return render_template("index.html", weather_data=weather_data)

    # Render 'index.html' template without weather data
    return render_template("index.html")


def get_weather(city):
    # Retrieve API key from environment variables
    api_key = os.getenv("API_KEY")

    # Construct API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # Send GET request to API
    response = requests.get(url)

    # Parse response JSON
    data = json.loads(response.text)

    # Check if weather and temperature data is available
    if "weather" in data and "temp" in data["main"]:
        # Calculate temperature in Celsius
        temperature = round(data["main"]["temp"] - 273.15, 2)

        # Retrieve humidity
        humidity = data["main"]["humidity"]

        # Retrieve wind speed
        wind_speed = data["wind"]["speed"]
    else:
        # Set temperature to 'N/A' if data is not available
        temperature = "N/A"

        # Set humidity to 'N/A' if data is not available
        humidity = "N/A"

        # Set wind speed to 'N/A' if data is not available
        wind_speed = "N/A"

    # Check if weather description is available
    if "weather" in data and len(data["weather"]) > 0:
        # Retrieve weather description
        description = data["weather"][0]["description"]

        # Retrieve weather icon
        icon = data["weather"][0]["icon"]
    else:
        # Set description to 'N/A' if data is not available
        description = "N/A"

        # Set icon to 'N/A' if data is not available
        icon = "N/A"

    # Create dictionary containing weather information
    weather_data = {
        "city": city,
        "temperature": temperature,
        "description": description.title(),
        "icon": icon,
        "humidity": humidity,
        "wind_speed": wind_speed,
    }

    # Return weather data dictionary
    return weather_data


if __name__ == "__main__":
    # Run the Flask application if script is executed directly
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
