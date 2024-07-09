import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USER_NAME= "hoangg"
TOKEN = "asdfghjkl12345678"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#create user name
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#Call /v1/users/<username>/graphs/<graphID>
today = datetime.now().strftime("%Y%m%d")
pixel_creattion_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today,
    "quantity": input("How many hours did you code today?"),
}
# response = requests.post(url=pixel_creattion_endpoint, json=pixel_data,headers=headers)
# print(response.text)

#edit pixel
#/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
pixel_update = {
    "quantity":"5",
}
# response = requests.put(url=pixel_update_endpoint,json=pixel_update,headers=headers)
# print(response.text)

#delete pixel
delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)