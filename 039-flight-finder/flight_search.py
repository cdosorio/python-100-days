from datetime import datetime
import string
import requests
from flight_data import FlightData

TEQUILA_API_KEY = "xl37pO8m67RcNGGlFhoJhuPX-gS05Rkc"
TEQUILA_BASE_URL = "https://tequila-api.kiwi.com"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_city_code(self, cityName: string):
        headers = {
        "apikey":TEQUILA_API_KEY,
        "accept": "application/json"
        }
        params = {        
        "term":cityName,
        "location_types":"city",
        "locale":"en-US",
        "limit":10,
        "active_only":"true",
        "max_stopovers":0
        }       
        
        location_endpoint = "/locations/query"
        
        response = requests.get(url=f"{TEQUILA_BASE_URL}{location_endpoint}", params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["locations"][0]["code"]
        
    def search_lowest_price(self, fly_from, fly_to, date_from:datetime, date_to:datetime ):
        print(f"search_lowest_price: {fly_from} -> {fly_to}")
        headers = {
            "apikey":TEQUILA_API_KEY,
            "accept": "application/json"
        }
        search_params = {        
            "fly_from":fly_from,
            "fly_to":fly_to,
            "dateFrom":date_from.strftime('%d/%m/%Y'),
            "dateTo":date_to.strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        search_endpoint = "/v2/search"
        response = requests.get(url=f"{TEQUILA_BASE_URL}{search_endpoint}", params=search_params, headers=headers)
        response.raise_for_status()
        data = response.json()
        flights_list = data["data"] #flights array

        try:
          cheaper_flight = min(flights_list, key=lambda x: x["price"])
        except:
          print('No flight found')
          return None
        else:
            flight_data = FlightData(
                price=cheaper_flight["price"],
                origin_city=cheaper_flight["route"][0]["cityFrom"],
                origin_airport=cheaper_flight["route"][0]["flyFrom"],
                destination_city=cheaper_flight["route"][0]["cityTo"],
                destination_airport=cheaper_flight["route"][0]["flyTo"],
                out_date=cheaper_flight["route"][0]["local_departure"].split("T")[0],
                return_date=cheaper_flight["route"][1]["local_departure"].split("T")[0]
            )
            print(f"Cheaper flight: {flight_data.destination_city}: {flight_data.price}")
            return flight_data