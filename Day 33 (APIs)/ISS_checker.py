import requests
import datetime as dt
import smtpd
from email import password, my_email, rec_email


response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
#200 prints, which is a status code

#Reading data 
data = response.json()
print(data)

specific_data = response.json()['iss_position']
print(specific_data)

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])
 

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
sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])

print(sunrise, sunset)

#Get Current time:
time_now = str(dt.datetime.now())
present_hour = int(time_now.split(" ")[1].split(":")[0])
print(present_hour)

#Email Logic



# with smtplib.SMTP('smtp.gmail.com',587) as connection:

#     #This encrypts our email
#     connection.starttls()
#     connection.login(user = my_email, password= password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=rec_email, 
#                         msg = "Subject:Hello!\n\nHello World")



#ISS Checker

if present_hour >= sunrise or present_hour <= sunset:
    if iss_latitude <= 37 and iss_latitude >= 28 and iss_longitude <= 102 and iss_latitude >= 92:
        pass






