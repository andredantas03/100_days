from http.client import responses

from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import json

load_dotenv("../.env")

APP_ID = os.getenv("NUTRITIONIX_ID")
API_KEY = os.getenv("NUTRITIONIX_KEY")
API_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
GENDER = 'male'
WEIGHT_KG = 92.3
HEIGHT_CM = 178
AGE = 34
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]
GOOGLE_SHEET_NAME = "workouts"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

#description = input("tell me which exercise you did? ")

query = {
    'query':'I  ran 3 miles',
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(API_URL,json=query,headers=headers)
response.raise_for_status()
data = response.json()
print(f"Nutritionix API call: \n {data} \n")

today = datetime.now()
for i in data['exercises']:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
          "date": today.strftime("%d/%m/%Y"),
          "time": today.strftime("%H:%M:%S"),
          "exercise": i['name'].title(),
          "duration": i['duration_min'],
          "calories": i['nf_calories']
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    sheet_response = requests.post(sheet_endpoint,data=json.dumps(sheet_inputs),headers=headers)
    sheet_response.raise_for_status()
