import requests
import json

api_key = json.load(open(".venv/environment_variables.json"))["api_key"]
munincipality = input("Enter the munincipality: ")

geocoding_request = f"http://api.openweathermap.org/geo/1.0/direct?q={munincipality}&limit={1}&appid={api_key}"
coordinates = requests.get(geocoding_request).json()[0]
lat = coordinates["lat"]
lon = coordinates["lon"]

weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
weather = requests.get(weather_request).json()
print(f"Weather: {weather['weather'][0]['description']}\nTemperature: {round(weather['main']['temp'] - 273.15)} Degrees Celsius")
