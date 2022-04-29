import requests
from datetime import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv("H:/Python/.env")

# Private keys
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
sheety_endpoint = os.getenv("sheety_endpoint")
exercise_endpoint = os.getenv("exercise_endpoint")


GENDER = "male"
WEIGHT_KG = 82
HEIGHT_CM = 177.80
AGE = 27



headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("What did you exercise: ")

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)

res = response.json()["exercises"]
today = dt.now()

bearer_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in res:
    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    exercise_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=bearer_headers)
