from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta


DEPATURE_CITY = "London"

#fetching flight data 
flight_search = FlightSearch()

#retrive data from google sheet and update iatacode
datamanager = DataManager()
sheet_Data = datamanager.get_destination_data() #retrieve data from google sheet
for row in sheet_Data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.search_iatacode(row["city"])
        print(f"Iatacode of {row["city"]} is {row['iataCode']}")
datamanager.destination_data = sheet_Data
update_message = datamanager.update_destination_code()

#find the lowest price of each city
tomorrow = datetime.now() + timedelta(days=1)
noti = NotificationManager("hynuiux@gmail.com")

for city in sheet_Data:
    flights = flight_search.price_searching(DEPATURE_CITY,city["city"],tomorrow)
    lowest_price = find_cheapest_flight(flights)
    if lowest_price.price is None:
        continue
    if lowest_price.price < city["lowestPrice"] and city["iataCode"]!= None:
        print("The lowest price now is", lowest_price.price)
        message = f"Subject: The lowest price \n\n The lowest price from {DEPATURE_CITY} to {city["city"]} is ${lowest_price.price} "
        noti.sendemai(message)