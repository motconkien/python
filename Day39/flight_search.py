import requests
from datetime import datetime, timedelta
from flight_data import FlightData

API_KEY = "qTbBfjdgbv9nijZFkVRx3TxPKUeNGQ7P"
API_SECRET = "EX2X8KpDpQANAsbh"
iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"

class FlightSearch:
    def __init__(self):
        self._api_key = API_KEY
        self._api_secret = API_SECRET
        self._token = self.get_access_token()
        self.headers = {
            "Authorization": f"Bearer {self._token}"}
        
    def get_access_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }
        response = requests.post(token_endpoint, headers=headers, data=data)
        return response.json()["access_token"]

    def search_iatacode(self,city_name):
        """Return city code"""
        parameters = {
            "subType": "CITY",
            "keyword": city_name
        }

        airport_params = {
            "subType": "AIRPORT",
            "keyword": city_name
        }
        response = requests.get(iata_endpoint,params=parameters, headers=self.headers)
        response.raise_for_status()
        locations = response.json()

        airport_response = requests.get(iata_endpoint,params=airport_params,headers=self.headers)
        airport_response.raise_for_status()
        airports = airport_response.json()

        for location in locations.get("data"):
            if location['address']['cityName'].upper() == city_name.upper():
                return location["iataCode"]
        
        #maybe not need, will be deleted then
        # for airport in airports.get("data"):
        #     if airport["address"]["cityName"].upper() == city_name.upper():
        #         airport_code =  airport["iataCode"]
        
        return None
            
    def price_searching(self,departurecity,arrivecity,departure_date):
        flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        departure_iatacode = self.search_iatacode(departurecity)
        arrival_iatacode = self.search_iatacode(arrivecity)
        
        parameters = {
            "originLocationCode": departure_iatacode,
            "destinationLocationCode": arrival_iatacode,
            "departureDate": departure_date,
            "adults": 1,
            "currencyCode": "USD"
        }
        
        response = requests.get(flight_endpoint,params=parameters,headers=self.headers)
        response.raise_for_status()
        flight_data = response.json()

        price_list = []
        for flight in flight_data["data"]:#["itineraries"][0]['segments']:
            price = flight["price"]["total"]
            price_list.append(price)
            min_price= min(price_list)
            return min_price



