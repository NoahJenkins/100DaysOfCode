from api_key import nutrition_ID, nutrition_key
import requests

api_headers = {
    "x-app-id": nutrition_ID,
    "x-app-key": nutrition_key
}

food_endpoint = "https://trackapi.nutritionix.com/v2/search/instant"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("What type of work out did you do do?\n")

parameters = {
 "query":exercise,
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response = requests.post(url=exercise_endpoint, headers=api_headers, json=parameters)
response.raise_for_status()
result = response.json()
print(result)