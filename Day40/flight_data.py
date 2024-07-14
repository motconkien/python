class FlightData:
    def __init__(self, depCode, arrCode, depDate, returnDate,price,stops):
        self.depcode = depCode
        self.arrcode = arrCode
        self.depdate = depDate
        self.returndate = returnDate
        self.price = price
        self.stops = stops

def find_cheapest_flight(flightdata):
    if flightdata is None or not flightdata['data']:
        print("There is no flight")
        return flightdata(None, None, None, None, None, None)
    
    first_flight = flightdata['data'][0]
    dep_code = first_flight['itineraries'][0]['segments'][0]["departure"]['iataCode']
    lowest_price = float(first_flight["price"]['grandTotal'])
    dest_code = first_flight['itineraries'][0]['segments'][0]["arrival"]['iataCode']
    out_date = first_flight['itineraries'][0]['segments'][0]["departure"]['at'].split('T')[0]
    re_date = first_flight['itineraries'][0]['segments'][0]["arrival"]['at'].split('T')[0]
    stops = len(first_flight['itineraries'][0]['segments'])-1

    cheapest_flight = FlightData(dep_code,dest_code,out_date,re_date,lowest_price,stops)

    for flight in flightdata['data']:
        price = float(flight['price']['grandTotal'])
        if price < lowest_price:
            lowest_price = price
            dep_code = flight['itineraries'][0]['segments'][0]["departure"]['iataCode']
            dest_code = flight['itineraries'][0]['segments'][0]["arrival"]['iataCode']
            out_date = flight['itineraries'][0]['segments'][0]["departure"]['at'].split('T')[0]
            re_date = flight['itineraries'][0]['segments'][0]["arrival"]['at'].split('T')[0]
            stops = len(flight['itineraries'][0]['segments'])-1
            cheapest_flight = FlightData(dep_code,dest_code,out_date,re_date,lowest_price, stops)
    return cheapest_flight