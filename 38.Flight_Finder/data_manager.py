import  requests
import os
from flight_search import FlightSearch

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.headers ={
            "Authorization": f"Bearer {os.getenv('ENV_SHEETY_PRICES_KEY')}"
        }

    def get_destination_data(self):
        response = requests.get(url=os.getenv('ENV_SHEETY_PRICES_API'), headers=self.headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_sheet(self, flight_searcher: FlightSearch):
        for i in range(0,len(self.destination_data)):
            if self.destination_data[i]["iataCode"] == "":
                self.destination_data[i]["iataCode"] = flight_searcher.get_iata_code(row["city"])
                line = {
                    'price': {
                        'city': self.destination_data[i]['city'],
                        'iataCode':self.destination_data[i]['iataCode'],
                        'lowestPrice':self.destination_data[i]['lowestPrice'],
                        'id': self.destination_data[i]['id'],
                        'departure': self.destination_data[i]['departure'],
                        'return' : self.destination_data[i]['return']
                    }
                }
                url = f'{os.getenv('ENV_SHEETY_PRICES_API')}/{self.destination_data[i]['id']}'
                response = requests.put(url, json=line, headers=self.headers)
                response.raise_for_status()


    def update_iata_code(self, flight_searcher: FlightSearch):
        for i in range(0,len(self.destination_data)):
            if self.destination_data[i]["iataCode"] == "":
                self.destination_data[i]["iataCode"] = flight_searcher.get_iata_code(self.destination_data[i]["city"])
                line = {
                    'price': {
                        'city': self.destination_data[i]['city'],
                        'iataCode':self.destination_data[i]['iataCode'],
                        'lowestPrice':self.destination_data[i]['lowestPrice'],
                        'id': self.destination_data[i]['id'],
                        'departure': self.destination_data[i]['departure'],
                        'return' : self.destination_data[i]['return']
                    }
                }
                url = f'{os.getenv('ENV_SHEETY_PRICES_API')}/{self.destination_data[i]['id']}'
                response = requests.put(url, json=line, headers=self.headers)
                response.raise_for_status()

    def update_row(self,cheapest_flight, destination_id):
        row_to_be_updated = self.destination_data[destination_id-2]

        row_to_be_updated['lowestPrice'] = cheapest_flight.price
        row_to_be_updated['departure'] = cheapest_flight.out_date
        row_to_be_updated['return'] = cheapest_flight.return_date

        row = {
            'price': {
                'city': row_to_be_updated['city'],
                'iataCode': row_to_be_updated['iataCode'],
                'lowestPrice': row_to_be_updated['lowestPrice'],
                'id': row_to_be_updated['id'],
                'departure': row_to_be_updated['departure'],
                'return': row_to_be_updated['return']
            }
        }
        print(row)
        url = f'{os.getenv('ENV_SHEETY_PRICES_API')}/{row_to_be_updated['id']}'
        response = requests.put(url, json=row, headers=self.headers)
        response.raise_for_status()

