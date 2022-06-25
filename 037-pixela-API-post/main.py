import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "cdosoriob"
TOKEN = "ktsd8tvfd9"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN":TOKEN
}

# 1.CREATE USER
# user_params = {
#   "token": TOKEN,
#   "username": USERNAME,
#   "agreeTermsOfService": "yes",
#   "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# 2.CREATE GRAPH
#$ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu"}'

# graph_params = {
#   "id": GRAPH_ID,
#   "name": "Cycling Graph1",
#   "unit": "Km",
#   "type": "float",
#   "color": "shibafu"
# }

# headers = {
#     "X-USER-TOKEN":TOKEN
# }

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# 3.SEE GRAPH
# https://pixe.la/v1/users/cdosoriob/graphs/graph1


# 4.POST A PIXEL
 #https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

# today = datetime.today()
# day2 = datetime(year=2022, month=1, day=15)

# pixel_update_params = {
#   "date": day2.strftime('%Y%m%d'),
#   "quantity": "2",
# }

# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)


# 5.UPDATE A PIXEL
 #https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5"}'

_date = datetime(year=2022, month=1, day=15)

pixel_update_params = {  
  "quantity": "22",
}

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{_date.strftime('%Y%m%d')}"
response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
print(response.text)