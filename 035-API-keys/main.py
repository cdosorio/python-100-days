#import json
import os
import requests
from twilio.rest import Client

MY_LAT = -31.448891 
MY_LONG = -72.669266 
OWM_API_KEY = os.environ.get("OWM_API_KEY")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


parameters = {
            "lat": MY_LAT,
            "lon": MY_LONG,
            "appid"   :OWM_API_KEY,
            "exclude":"current,minutely,daily"          
        }
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
#print(data["hourly"][0]["weather"][0]["id"])
#json_formatted_str = json.dumps(data, indent=2)
#print(json_formatted_str)
weather_0h_12h = data["hourly"][:12]
codes_0h_12h =  [item["weather"][0]["id"] for item in weather_0h_12h] 
print(codes_0h_12h)
will_rain = any(ele > 700 for ele in codes_0h_12h) # < 700
if will_rain:
    print("sending SMS...")
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
                    .create(
                        body="Its going to rain today...",
                        from_='+17473024549',
                        to='+56977964322'
                    )

    print(message.status)
