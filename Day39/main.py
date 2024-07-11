import requests
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
APP_ID = "59643256"
AOO_KEY = "9965128e0d1758f03feb776c695ee5b0"

ENDPOINT = "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/flightDeals/prices"


token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"

#test sheety 
# response_sheet = requests.get(url=ENDPOINT)
# response_sheet.raise_for_status()
# result = response_sheet.json()['prices']
#add rows 
# for row in result:
#     if row['iataCode'] == "":
#         row['iataCode'] = "TESTING"
API_KEY = "qTbBfjdgbv9nijZFkVRx3TxPKUeNGQ7P"
API_SECRET = "EX2X8KpDpQANAsbh"


# pprint(response.json()['data'][0]["iataCode"])
# print(access_token)


# pprint(result)




#test amadeus
flight = FlightSearch()
codepa = flight.search_iatacode("Paris")
codelon = flight.search_iatacode("London")
flight_data = flight.price_searching("Paris","London","2024-08-01")
# print(codelon,codepa)
for flight in flight_data["data"][0]["itineraries"][0]['segments'][:2]:
    print(flight)