import requests
from dotenv import load_dotenv
from os import getenv
from datetime import datetime
load_dotenv("../.env")
PIXELA_USER_TOKEN = getenv("PIXELA_USER_TOKEN")
USERNAME = 'usefullusername121'
GRAPH_ID = 'graph1'

pixela_endpoint ="https://pixe.la/v1/users"

user_params = {
            'token': PIXELA_USER_TOKEN,
            'username': 'usefullusername121',
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes'
}

# response = requests.post(url = pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id" : "graph1",
#     "name" : "Cycling Graph",
#     "unit" : "Km",
#     "type" : "float",
#     "color" : "ajisai"
# }
#
headers = {
    'X-USER-TOKEN' : PIXELA_USER_TOKEN
}
#
# response = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
# post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# post_config ={
#     "date" : today.strftime("%Y%m%d"),
#     "quantity" : "1.9"
# }
#
# response = requests.post(url=post_endpoint,json=post_config,headers=headers)
# print(response.text)

# put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
#
# put_config = {
#     "quantity" : "3.1"
# }
#
# response = requests.put(url=put_endpoint,json=put_config,headers=headers)
# print(response.text)
