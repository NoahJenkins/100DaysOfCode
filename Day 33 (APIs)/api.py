import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#200 prints, which is a status code

#Reading data 
data = response.json()
print(data)

specific_data = response.json()['iss_position']
print(specific_data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position) 

#The below URL is not correct
# bad_response = requests.get(url="http://api.open-notify.org/iss-now.jso")
# bad_response.raise_for_status()

#Response codes:
# 1xx = hold open
# 2xx = Here you go 
# 4xx = You (user) screwed up 
# 5xx: I (the webstire/service) screwed up