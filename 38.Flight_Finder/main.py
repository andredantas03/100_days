import time
from flight_data import find_cheapest_flight
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv("../.env")



# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_searcher = FlightSearch()
print(sheet_data)
# Set your origin airport
ORIGIN_CITY_IATA = "LON"

# ==================== Update the Airport Codes in Google Sheet ====================


# for row in sheet_data:
#     if row["iataCode"] == "":
#         row["iataCode"] = flight_searcher.get_iata_code(row["city"])
#         # slowing down requests to avoid rate limit
#         time.sleep(2)
# print(f"sheet_data:\n {sheet_data}")
#


# ==================== Search for Flights ====================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_searcher.search_flights(
        from_time=tomorrow,
        to_time=six_month_from_today,
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"]
    )
    print(f"The actual lowest price for {destination['city']}: is £{destination['lowestPrice']}")
    cheapest_flight = find_cheapest_flight(flights)
    print(f"the price founded today for {destination['city']}: is £{cheapest_flight.price}")
    if cheapest_flight.price!="N/A" and cheapest_flight.price<float(destination['lowestPrice']):
        data_manager.update_row(cheapest_flight,destination["id"])
    # Slowing down requests to avoid rate limit
    time.sleep(2)



