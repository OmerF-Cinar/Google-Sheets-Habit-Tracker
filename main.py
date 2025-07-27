import requests
from datetime import datetime
import os

now = datetime.now()

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
DATE = now.strftime("%d/%m/%Y")
TIME = now.strftime("%H:%M:%S")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
    "Content-Type": "application/json"
}

QUERY = input("Tell me of your exercise today.")

parameters = {
    "query" : QUERY,
    "weight_kg" : 82,
    "height_cm" : 178,
    "age" : 22
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)

result = response.json()

sheety_endpoint = os.environ["SHEETY_ENDPOINT"] #This should link to your own personal google sheet.

headers = {
        "Authorization" : f"Basic {os.environ['TOKEN']}" #I had used Basic authorization, but you can use Bearer auth as well.
}

for exercise in result["exercises"]:
    params = {
            "workout" : {
                    "date" : DATE,
                    "time" : TIME,
                    "exercise" : exercise["name"].title(),
                    "duration" : exercise["duration_min"],
                    "calories" : exercise["nf_calories"],
                    "id" : "3"
            }
    }


response_sheety = requests.post(url=sheety_endpoint, json=params, headers=headers)

