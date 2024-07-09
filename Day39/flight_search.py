import requests

API_KEY = "qTbBfjdgbv9nijZFkVRx3TxPKUeNGQ7P"
API_SECRET = "EX2X8KpDpQANAsbh"
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self): 
        self._api_key = API_KEY
        self._api_secret = API_SECRET
        self._token = self.get_new_token()
    
    def get_new_token(self):
        self.header = {
            'Content-Type':'application/x-www-form-urlencoded'
        }
        self.body = {
            'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret':API_SECRET
        }
        response = requests.post(url=token_endpoint, headers= self.header, data = self.body)
        response.json()["access_token"]
    
    def get_destination_code(self,cityname):
        headers ={
            'Authorization': f"Bearer{self._token}"
        }
        
        parameters = {
            "keyword": cityname,
            "max":"2",
            "include": 'AIRPORTS',
        }
        response = requests.get(url=iata_endpoint, headers=headers,params=parameters)
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"Index error. Not found code for {cityname}")
            return "N/A"
        except KeyError:
            print(f"Keyerror: Not found code for {cityname} ")
            return "Not Found"
        
        return code