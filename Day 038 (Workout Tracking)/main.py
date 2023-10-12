from api_key import nutrition_ID, nutrition_key, sheet_token
import requests
from datetime import datetime as dt

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


if 'exercises' in result and result['exercises']:
    exercise_data = result['exercises'][0]
    calories = str(exercise_data.get("nf_calories", "N/A"))
    duration = str(exercise_data.get("duration_min", "N/A"))
    exercise_name = exercise_data.get("name", "N/A")

   # Printing the extracted information
    print(f'Exercise Name: {exercise_name}')
    print(f'Duration (min): {duration}')
    print(f'Calories: {calories}')
else:
    print("No exercise data found in the response.")

##########################################

today = dt.now()
today.now
# print(today)

date = today.strftime('%d/%m/%Y')
print(date)

military_time = today.strftime('%H:%M:%S')
print(military_time)

############################################

sheet_endpoint = "https://api.sheety.co/ac6b17b343d7dd5b605bfbbfdc1535b5/workoutTracking/workouts"
sheet_key = {
"Authorization": f"Bearer {sheet_token}"
}

sheet_response = requests.get(url=sheet_endpoint, headers=sheet_key)
sheet_response.raise_for_status()
sheet_data = sheet_response.json()
print(sheet_data)

sheet_params = {
    'workout': {
        'date': date, 
        'time': military_time, 
        'exercise': exercise_name, 
        'duration': duration, 
        'calories': calories}}

sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_key)
sheet_response.raise_for_status()
sheet_data = sheet_response.json()
print(sheet_data)