import datetime
import requests
from flight_search import FlightSearch

SHEETY_BASE_URL = "https://api.sheety.co/9a58efae000087421425a9fd22e83a95/flightDeals"

class DataManager:
    
    def __init__(self, flight_search:FlightSearch) -> None:
        self.searcher = flight_search

    def get_cities(self):
        response = requests.get(url=f"{SHEETY_BASE_URL}/prices/")
        response.raise_for_status()
        destinations_list = response.json()["prices"]

        #for each sheet record, update with city code
        for destination in destinations_list:            
            if destination["iataCode"]=="":
                city = destination["city"]
                id = destination["id"]
                print(f"{city} dont have a code. Searching with API...")
                code = self.searcher.get_city_code(city)
                destination["code"] = code
                print(f"Found code {code}. Updating with API...")                
                params = {
                    "price":{
                        "iataCode":code
                    }                    
                }                    
                response = requests.put(url=f"{SHEETY_BASE_URL}/prices/{id}", json=params)
                response.raise_for_status()
                
        return destinations_list

    def search_flights(self, fly_from, destination, dateFrom:datetime, dateTo:datetime):        
            dest_city = destination["city"]
            dest_stored_price = destination["lowestPrice"]
            print(f"Searching flights to {dest_city} ...")
            cheaper_flight = self.searcher.search_lowest_price(fly_from, destination["iataCode"], dateFrom, dateTo) 
            
            if cheaper_flight is not None:    
                cheaper_flight_price = cheaper_flight.price    
                #cheaper_flight_date = cheaper_flight[1]     
                if cheaper_flight_price < dest_stored_price:
                    return cheaper_flight
                else:
                    return None
            else:
                return None

    def create_user(self, first_name, last_name, email):
        sheety_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,	
                "email" : email
            }
        }
        
        sheety_response = requests.post(url=f"{SHEETY_BASE_URL}/users", json=sheety_params)
        sheety_response.raise_for_status()
        print(sheety_response.text)

    def get_users(self):
        response = requests.get(url=f"{SHEETY_BASE_URL}/users")
        response.raise_for_status()
        users_list = response.json()["users"]
        print(f"Users found: {len(users_list)}")
        return users_list
    
