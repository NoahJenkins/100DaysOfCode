import requests
from api_key import sheety_token

token = sheety_token
sheet_endpoint = "https://api.sheety.co/ac6b17b343d7dd5b605bfbbfdc1535b5/flightPriceChecker/trips"
sheet_key = {
"Authorization": f"Bearer {sheety_token}"
}



response = requests.get(url=sheet_endpoint, headers=sheet_key)
response.raise_for_status()
get_data = response.json()
print(get_data)



sheet_params = {         
    'trip': {
    'city': "dummy",
    'iataCode': "test",
    'lowestPrice': "42",
            }
    }

post_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_key)
post_response.raise_for_status()
post_data = post_response.json()
print(post_data)