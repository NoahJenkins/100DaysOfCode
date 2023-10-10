# A Get request recieves data, a post request post data to a source. 
#Put is used to updat existing data. 
#Delete is self explanatory, it deletes data. 

import requests
from api_key import token, username


#Creating Pixe.la User
# pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)