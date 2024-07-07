import requests
import json

response = requests.get(url= "https://zenquotes.io/api/random")
response.raise_for_status()
data = response.json()
quote = data[0]['q']