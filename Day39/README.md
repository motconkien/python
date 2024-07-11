CAPSTONE PART 1 - Cheap Flight Finder
Program Requirements
1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.

4. The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates. e.g.

API list:
1. Sheety API:
link: "https://api.sheety.co/f33ae462d27ae5425f8bd7c6ffe10652/flightDeals/prices"
APP_ID = "59643256"
API_KEY = "9965128e0d1758f03feb776c695ee5b0"
2. Amadeus API
API_KEY = "qTbBfjdgbv9nijZFkVRx3TxPKUeNGQ7P"
API_SECRET = "EX2X8KpDpQANAsbh"
link: 
token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"