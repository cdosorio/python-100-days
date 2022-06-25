import requests
from datetime import datetime

MY_LAT = 51
MY_LNG = 43

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0]) #24 HH

time_now = datetime.now()
print(time_now.hour)


