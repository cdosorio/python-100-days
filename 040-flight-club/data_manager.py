import requests

SHEETY_BASE_URL = "https://api.sheety.co/9a58efae000087421425a9fd22e83a95/flightDeals"

class DataManager:
    
    def __init__(self) -> None:
        pass

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

    

    


    
