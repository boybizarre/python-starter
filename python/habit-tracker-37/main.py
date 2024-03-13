import requests
from datetime import datetime


USERNAME = "boybizarre"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
CREATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
TOKEN = "overeightcharactertoken"

# date = datetime(year=2024, month=2, day=25)
date = datetime.now()

UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"
DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"

user_json = {
    "token": "overeightcharactertoken",
    "username": "boybizarre",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
  }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_json)
# print(response.text)

graph_json = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

create_pixel_json = {
    "date": date.strftime("%Y%m%d"),
    "quantity": "4",
}

new_pixel_json = {
  "date": date.strftime("%Y%m%d"),
  "quantity": "15",
}


graph_headers = {
  "X-USER-TOKEN": TOKEN,
}


# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_json, headers=graph_headers)
# print(response.text)

# response = requests.post(url=CREATE_PIXEL_ENDPOINT, json=create_pixel_json, headers=graph_headers)
# print(response.text)

# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=new_pixel_json, headers=graph_headers)

# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=graph_headers)
# print(response.text)
