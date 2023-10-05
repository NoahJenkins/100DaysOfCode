import requests
import datetime as dt
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# #200 prints, which is a status code

# #Reading data 
# data = response.json()
# print(data)

# specific_data = response.json()['iss_position']
# print(specific_data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position) 

# #The below URL is not correct
# # bad_response = requests.get(url="http://api.open-notify.org/iss-now.jso")
# # bad_response.raise_for_status()

# #Response codes:
# # 1xx = hold open
# # 2xx = Here you go 
# # 4xx = You (user) screwed up 
# # 5xx: I (the webstire/service) screwed up


# Sun Set Sun Down

MY_LAT = 32.749901
MY_LONG = 97.330338

parameters = { "lat":MY_LAT, 
              "long":MY_LONG,
              "formatted": 0
             }

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)

response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split('T')[1].split(":")[0]
sunset = data["results"]["sunset"].split('T')[1].split(":")[0]

print(sunrise, sunset)

# time_now = dt.datetime.now()
# print(time_now)


