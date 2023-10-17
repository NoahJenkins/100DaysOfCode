import requests
from api_key import sheety_token

SHEETY_USER_ENDPOINT = "https://api.sheety.co/ac6b17b343d7dd5b605bfbbfdc1535b5/flightPriceChecker/users"

sheet_key = {
"Authorization": f"Bearer {sheety_token}"}

#test
# response = requests.get(url=SHEETY_USER_ENDPOINT, headers= sheet_key)
# response.raise_for_status()
# data = response.json()
# print(data)

# Adding customer
def user_input():
    global f_name, l_name, email_1, email_2
    f_name = input("What if your first name?\n")
    l_name = input("What if your last name?\n")
    email_1 = input("What if your email?\n")
    email_2 = input("Please validate your email by typing it in again?\n")

    if email_1 == email_2:
        pass
    else:
        print("I am sorry, your emails did not match, please try again")
        user_input()

user_input()
    
params = {
            "user":{
                "firstName": f_name,
                "lastName" : l_name,
                "email": email_1
            }}

print(params)

response = requests.post(url=SHEETY_USER_ENDPOINT, headers= sheet_key, json=params)
response.raise_for_status()
data = response.json()
print(data)
