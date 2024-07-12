import requests

ENDPOINT = "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {} #sheetdata
        
    def get_destination_data(self):  
        response = requests.get(url=ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_code(self):
        for city in self.destination_data:
            sheet_inputs = {
                "price": {  
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{ENDPOINT}/{city['id']}", json=sheet_inputs)
            response.raise_for_status()  # Ensure that any request errors are raised
        return "Update complete"  # Return a success message after the loop completes


if __name__ == "__main__":
    test = DataManager()
    print(test.get_destination_data())