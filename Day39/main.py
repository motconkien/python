import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

APP_ID = "59643256"
AOO_KEY = "9965128e0d1758f03feb776c695ee5b0"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

for row in sheet_data:
    if row["iatacode"] == "":
        pass