import requests

ENDPOINT = "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/flightDeals/prices"
MAIL_ENPOINT = "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/flightDeals/users"

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.customers_email = {}
    
    def get_destination_data(self):
        response = requests.get(url=ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_data(self):
        for city in self.destination_data:
            sheet_inputs = {
                "price": {
                    "iataCode":city["iataCode"]
                }
            }
            response = requests.put(f"{ENDPOINT}/{city["id"]}", json=sheet_inputs)
            response.raise_for_status()
        return "Update completed"
    
    def get_customer_emails(self):
        response = requests.get(url=MAIL_ENPOINT)
        response.raise_for_status()
        customers_email = response.json()
        self.customers_email = customers_email["users"]
        return self.customers_email

if __name__ == "__main__":
    test = DataManager()
    print(test.get_customer_emails())
