import requests
from api_key import sheety_token

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ac6b17b343d7dd5b605bfbbfdc1535b5/flightPriceChecker/trips"



class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.sheet_key = {
"Authorization": f"Bearer {sheety_token}"}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers= self.sheet_key)
        data = response.json()
        self.destination_data = data["trips"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
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
