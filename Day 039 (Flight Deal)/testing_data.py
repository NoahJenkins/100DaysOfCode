import requests
from api_key import sheety_token


class DataManager:
    def __init__(self):
        self.token = sheety_token
        self.sheet_endpoint = "https://api.sheety.co/ac6b17b343d7dd5b605bfbbfdc1535b5/flightPriceChecker/trips"
        self.sheet_key = {
"Authorization": f"Bearer {sheety_token}"
}


    def get_data(self):
        response = requests.get(url=self.sheet_endpoint, headers=self.sheet_key)
        response.raise_for_status()
        get_data = response.json()
        print(get_data)

    def post_data(self, city, iataCode, price):
        sheet_params = {
            'trip': {
                'city': city,
                'iataCode': iataCode,
                'lowestPrice': price
            }
        }
        response = requests.post(url=self.sheet_endpoint, headers=self.sheet_key, json=sheet_params)
        response.raise_for_status()
        post_data = response.json()
        print(post_data)

    def put_data(self, city, iataCode, price):
        sheet_params = {
            'trip': {
                'city': city,
                'iataCode': iataCode,
                'lowestPrice': price
            }
        }
        response = requests.put(url=f'{self.sheet_endpoint}/2', headers=self.sheet_key, json=sheet_params)
        response.raise_for_status()
        put_data = response.json()
        print(put_data)




#Test Code
test = DataManager()
test.get_data()
# test.post_data("Dummy", "Par", "54")
# test.put_data(city= "Paris", iataCode= "DFW", price="54")