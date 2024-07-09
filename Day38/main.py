import requests
from datetime import datetime
import os

GENDER = "female"
WEIGHT_KG = "42"
HEIGHT_CM = "150"
AGE = "26"

APP_ID = os.environ("APP_ID") 
APP_KEY= os.environ("APP_KEY")

USER = os.environ("USER")
PASS = os.environ("PASS")


excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_enpoint = "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/mine/workouts"

headers = {
    'x-app-id': APP_ID,
    'x-app-key':APP_KEY
}

query = input("Tell me which excercise you did? ")
parameters = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm":HEIGHT_CM, 
    "age": AGE
}

response = requests.post(url=excercise_endpoint,headers=headers, json=parameters)
result = response.json()
today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")
for excercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today,
            "time":time_now,
            "exercise": excercise["name"].title(),
            "duration": excercise["duration_min"],
            "calories": excercise["nf_calories"]
        }
        
    }
    sheet_response = requests.post(sheet_enpoint, json=sheet_inputs, auth=(USER,PASS))
    print(sheet_response.text)
