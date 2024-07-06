import requests
import json

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url = "https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
#print(question_data)
with open("data.json", "w") as file:
    json.dump(question_data,file,indent=4)
    