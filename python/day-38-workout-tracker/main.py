import requests
import os
from datetime import datetime


APP_ID =os.environ.get('APP_ID')
API_KEY =os.environ.get('API_KEY')

print(os.environ.get('APP_ID'))

GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 25

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/505eccc4073ca009905272f76e394132/copyOfMyWorkoutsPython/workouts'

exercise_text = input('Tell us which exercise you did: ')

request_headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
}

request_body = {
  "query": exercise_text,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}

response = requests.post(exercise_endpoint, json=request_body, headers=request_headers)
data = response.json()
print(data);

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data['exercises']:
    sheet_json = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    } 

sheet_headers = {
  "Authorization": f"Bearer {API_KEY}"
}

sheet_response = requests.post(sheet_endpoint, json=sheet_json, headers=sheet_headers)
print(sheet_response.text)