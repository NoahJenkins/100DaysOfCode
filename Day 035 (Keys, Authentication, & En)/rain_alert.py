import requests
from api_key import KEY

# // https://api.openweathermap.org/data/2.5/weather?q=Dallas,us&APPID=KEY

parameters = { "q":"Dallas,us", 
              "APPID":KEY
             }

response = requests.get("https://api.openweathermap.org/data/2.5/weather?", params=parameters)
data = response.json()

print(data)