import requests
from datetime import datetime, timedelta


API_KEY = "qTbBfjdgbv9nijZFkVRx3TxPKUeNGQ7P"
API_SECRET = "EX2X8KpDpQANAsbh"
iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"

class FlightSearch:
    def __init__(self):
        self._api_key = API_KEY
        self._api_secret = API_SECRET
        self._token = self.get_access_token()
        self.headers = {
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json"
        }
        # Debugging print statement to verify token and headers
        print(f"Access Token: {self._token}")
        print(f"Headers: {self.headers}")
        
    def get_access_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(token_endpoint, headers=headers, data=data)
        response.raise_for_status()  # This will raise an error for bad status
        token = response.json().get("access_token")
        if not token:
            raise Exception("Failed to retrieve access token")
        return token
    
    def search_iatacode(self,cityname):
        airport_params = {
            "subType": "AIRPORT",
            "keyword": cityname
        }
        print(f"Searching airport code for {cityname}")
        response = requests.get(iata_endpoint, params=airport_params,headers=self.headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Error fetching airport code: {e}")
            print(f"Response content: {response.content}")
            return None
        
        airports= response.json()['data']
        for airport in airports:
            if airport['address']['cityName'].upper() == cityname.upper():
                return airport['iataCode']
        return None
    
    def price_searching(self,depature,arrival,fromdate,todate,is_direct = True):
        flight_endpoint =  "https://test.api.amadeus.com/v2/shopping/flight-offers"
        dep_code = self.search_iatacode(depature)
        arr_code = self.search_iatacode(arrival)
        dep_date = datetime.strftime(fromdate,"%Y-%m-%d")
        arr_date = datetime.strftime(fromdate,"%Y-%m-%d")

        if not dep_code or not arr_code:
            print("There is no airport code for the given cities")
            return None
        
        parameters = {
            "originLocationCode": dep_code,
            "destinationLocationCode": arr_code,
            "departureDate": dep_date,
            "returnDate": arr_date,
            "adults": 1,
            "currencyCode": "USD",
            "nonStop": "true" if is_direct else "false"
        }

        print(f"Searching price from {depature} to {arrival} on {fromdate} to {todate}")

        response = requests.get(flight_endpoint, params=parameters,headers=self.headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Failed to load data: {e}")
            print(f"Response content: {response.content}")
            return None

        flight_data = response.json()
        return flight_data

#test
if __name__ == "__main__":
    flight_search = FlightSearch()
    airport_code = flight_search.search_iatacode("London")
    print(f"Airport Code for London: {airport_code}")
