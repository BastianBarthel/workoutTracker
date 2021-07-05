import os
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
TOKEN = os.environ.get("TOKEN")

# Enter your specs
GENDER = "male"
WEIGHT = 80
HEIGHT = 188
AGE = 42

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")

exercise_input = input("Tell me about your exercises: ")

exercise_params = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_response.raise_for_status()
results = exercise_response.json()["exercises"]

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%H:%M:%S")

# You probably need to change line 45, see README.md for more information
for result in results:
    sheet_params = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": result["name"].title(),
            "duration": round(result["duration_min"]),
            "calories": round(result["nf_calories"]),
        }
    }

    sheet_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_headers)
