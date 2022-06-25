from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
#from flight_data import data

ORIGIN_CITY_IATA = "LON" #LONDON

flight_search = FlightSearch()
notification_manager = NotificationManager()
data_manager = DataManager(flight_search)

destination_lists = []
# step 1
destination_lists = data_manager.get_cities()
print(destination_lists)

# step 2 check for the cheapest flights from tomorrow to 6 months later
today = datetime.now()
date_from = (today + timedelta(days=1))
date_to = (today + relativedelta(months=6))

print(f"Searching from {date_from.strftime('%d/%m/%Y')} to {date_to.strftime('%d/%m/%Y')}")

for destination in destination_lists:   
    dest_city = destination["city"]
    flight = data_manager.search_flights(ORIGIN_CITY_IATA, destination, date_from, date_to)
    if flight is not None:
        msg = (f"Low price alert! Only ${flight.price}: to fly from {flight.origin_city} to {flight.destination_city}, "
            f"from {flight.out_date}") 
        #notification_manager.send_SMS(msg)

        #day 40-step 5: email all customers
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        users_list = data_manager.get_users()
        for user in users_list:
            notification_manager.send_email(user["email"], "New Low Price Flight", msg, link)

        break
    else:
        print("Nothing found")






