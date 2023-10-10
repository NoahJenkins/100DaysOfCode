# A Get request recieves data, a post request post data to a source. 
#Put is used to updat existing data. 
#Delete is self explanatory, it deletes data. 

import requests
from api_key import token, username
from datetime import datetime as dt

######################################################################################################
#Creating Pixe.la User
pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

######################################################################################################
#Creating Graph
graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

# graph_config = {
#     "id": "graph1",

#     "name": "Python Graph",
#     "unit": "Commits",
#     "type": "int",
#     "color": "shibafu"
# }

header = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

######################################################################################################
#Posting a Value to the Graph
# post_value_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'

# value_config = {
#     "date":"20231010",
#     "quantity": "3"
# }

# # reponse = requests.post(url=post_value_endpoint, headers= header, json=value_config)
# print(reponse.text)


######################################################################################################
#Posting a Value to the Graph with auto date

today = dt.now()
# print(today)

date = today.strftime('%Y%m%d')
print(date)

# post_value_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'

# value_config = {
#     "date":date,
#     "quantity": "5"
# }

# reponse = requests.post(url=post_value_endpoint, headers= header, json=value_config)
# print(reponse.text)

######################################################################################################
#Posting a Value to the Graph with auto date

today = dt.now()
# print(today)

date = today.strftime('%Y%m%d')
print(date)

# post_value_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1'

# value_config = {
#     "date":date,
#     "quantity": "5"
# }

# reponse = requests.post(url=post_value_endpoint, headers= header, json=value_config)
# print(reponse.text)
######################################################################################################
#Updating a Pixel using Put

put_value_endpoint = f'{pixela_endpoint}/{username}/graphs/graph1/20231010'

value_config = {
    "date":date,
    "quantity": "3"
}

reponse = requests.put(url=put_value_endpoint, headers= header, json=value_config)
print(reponse.text)