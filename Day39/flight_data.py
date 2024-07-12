 #attributes for price, departure_airport_code etc. Create a function called find_cheapest_flight()
class FlightData:
    def __init__(self,dep_code, dest_code, price, outbound_date):
        self.departure_airport_code = dep_code
        self.destination_airport_code = dest_code
        self.price = price
        self.outbound_date = outbound_date

def find_cheapest_flight(flight_data):
    """Data arguments will be json file. Assume that the first flight will have the lowest price"""
    if flight_data is None or not flight_data["data"]:
        print("No data for this flight")
        return FlightData(None,None,None,None)
    
    first_flight = flight_data['data'][0]
    dep_code = first_flight['itineraries'][0]['segments'][0]["departure"]['iataCode']
    lowest_price = float(first_flight["price"]['grandTotal'])
    dest_code = first_flight['itineraries'][0]['segments'][0]["arrival"]['iataCode']
    out_date = first_flight['itineraries'][0]['segments'][0]["departure"]['at'].split('T')[0]

    cheapest_flight = FlightData(dep_code,dest_code,lowest_price,out_date)

    for flight in flight_data["data"]:
        price = float(flight["price"]['grandTotal'])
        if price < lowest_price:
            lowest_price = price
            dep_code = flight['itineraries'][0]['segments'][0]["departure"]['iataCode']
            dest_code = flight['itineraries'][0]['segments'][0]["arrival"]['iataCode']
            out_date = flight['itineraries'][0]['segments'][0]["departure"]['at'].split('T')[0]
            cheapest_flight = FlightData(dep_code,dest_code,lowest_price,out_date)
    return cheapest_flight


