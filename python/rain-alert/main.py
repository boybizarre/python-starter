import requests
import os

api_key=os.environ.get('API_KEY')

weather_parameters  = {
    "lat": 6.524379,
    "lon": 3.379206,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella.')



print(response.status_code)
# print(data)