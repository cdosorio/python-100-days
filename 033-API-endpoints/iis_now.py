import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)

response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)



    