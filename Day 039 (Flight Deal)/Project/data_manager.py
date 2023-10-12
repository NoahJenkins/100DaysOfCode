import requests
from api_key import sheety_token

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ac6b17b343d7dd5b605bfbbfdc1535b5/flightPriceChecker/trips"



class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheet_key = {
"Authorization": f"Bearer {sheety_token}"}

    def get_destination_data(self):
        
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers= self.sheet_key)
        data = response.json()
        self.destination_data = data["trips"]
        
        return self.destination_data

    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "trip": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers= self.sheet_key
            )
            print(response.text)
