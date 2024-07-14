from data_manager import DataManager
from flight_data import FlightData, find_cheapest_flight
from flight_search import FlightSearch
from datetime import datetime,timedelta
from notification_manager import NotificationManager

DEPATURE_CITY = "LONDON"
DEPATURE_DATE = datetime.now()
RETURN_DATE = DEPATURE_DATE + timedelta(days = 30*6)

#fetching data
flight_data = FlightSearch()

#data from sheet
data = DataManager()
sheet_data = data.get_destination_data()
for row in sheet_data:
    if row["iataCode"] == None:
        row["iataCode"] = flight_data.search_iatacode(row["city"])
        print(f"Iatacode of {row["city"]} is {row['iataCode']}")

data.destination_data = sheet_data
update_data = data.update_destination_data()
user_mails = data.get_customer_emails()
for city in sheet_data:
    flights = flight_data.price_searching(DEPATURE_CITY,city["city"],DEPATURE_DATE,RETURN_DATE)
    lowest_flight = find_cheapest_flight(flights)
    if lowest_flight is None:
        print("There is no direct flight. Looking for indirect flight")
        flights = flight_data.price_searching(DEPATURE_CITY,city["city"],DEPATURE_DATE,RETURN_DATE, False)
        lowest_flight = find_cheapest_flight(flights)
        if lowest_flight is None:
            continue

    if lowest_flight.price < city['lowestPrice'] and city['iataCode'] is not None:
        for user in user_mails:
            email = user["whatIsYourEmail?"]
            noti = NotificationManager(email)
            message = f"Subject: The lowest price \n\n The lowest price from {DEPATURE_CITY} to {city["city"]} is ${lowest_flight.price} with {lowest_flight.stops} stops"
            noti.sendemail(message)