import requests

parameters = {
    "amount": 10,
    "type":"boolean"
}

response = requests.get('https://opentdb.com/api.php', params=parameters)
data = response.json()
# print(data['results'])

question_data = data['results']
