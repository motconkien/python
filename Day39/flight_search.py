import requests
from datetime import datetime
from flight_data import find_cheapest_flight

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

    def search_iatacode(self, city_name):
        """Return airport code for the given city name"""
        airport_params = {
            "subType": "AIRPORT",
            "keyword": city_name
        }

        # Debugging print statements
        print(f"Searching for airport code for: {city_name}")

        airport_response = requests.get(iata_endpoint, params=airport_params, headers=self.headers)
        try:
            airport_response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Error fetching airport code: {err}")
            print(f"Response content: {airport_response.content}")
            return None

        airports = airport_response.json()
        for airport in airports.get("data", []):
            if airport["address"]["cityName"].upper() == city_name.upper():
                return airport["iataCode"]

        return None  # Return None if no matching airport code is found

    def price_searching(self, departurecity, arrivecity, departure_date):
        """Return the json file"""
        flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        departure_airport_code = self.search_iatacode(departurecity)
        arrival_airport_code = self.search_iatacode(arrivecity)
        dep_date = datetime.strftime(departure_date, "%Y-%m-%d")

        if not departure_airport_code or not arrival_airport_code:
            print("Could not find airport codes for the given cities.")
            return None

        parameters = {
            "originLocationCode": departure_airport_code,
            "destinationLocationCode": arrival_airport_code,
            "departureDate": dep_date,
            "adults": 1,
            "currencyCode": "USD"
        }

        print(f"Searching for flights from {departurecity} to {arrivecity} on {departure_date}")

        response = requests.get(flight_endpoint, params=parameters, headers=self.headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Error fetching flight data: {err}")
            print(f"Response content: {response.content}")
            return None

        flight_data = response.json()
        return flight_data

#test
if __name__ == "__main__":
    flight_search = FlightSearch()
    airport_code = flight_search.search_iatacode("London")
    print(f"Airport Code for London: {airport_code}")

    flights = flight_search.price_searching("London", "Paris", datetime.now())
    print(f"Flights from London to Paris on 2024-08-01: {flights}")
    cheapest = find_cheapest_flight(flights)
    print(cheapest.price)
