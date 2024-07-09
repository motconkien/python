import requests

ENDPOINT = "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):  
        response = requests.get(url = ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "prices":{
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(f"{ENDPOINT}/{city['id']}",json = new_data)
            print(response.text)