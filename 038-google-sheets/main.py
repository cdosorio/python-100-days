from datetime import datetime
import requests

# 2. Get exercise stats from nutritionix API
APP_ID = "46acc847"
API_KEY = "c4314162f9b0034db69a1b3a47f0de2c"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id": "0"
}

my_exercise = input("Tell me which exercises you did: ")

exercise_params = {
 "query":my_exercise,
 "gender":"male",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":42
}

# print(exercise_params)


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
response.raise_for_status()
exercise_response = response.json()

exercises_list = exercise_response["exercises"]
#print(exercise_response)

# 4.Saving data with sheety API
print(f"Saving {len(exercises_list)} rows to sheet...")


for exercise in exercises_list:   
    #exit(0)
    name = exercise["name"]
    duration = float(exercise["duration_min"])
    calories = float(exercise["nf_calories"])
        
    today = datetime.now()
    today_str = today.strftime('%d/%m/%Y')
    now_str = today.strftime('%X')

    sheety_params = {
        "workout": {
        "date": today_str,
        "time": now_str,	
        "exercise" : name.title(),
        "duration" : duration,	
        "calories" : calories
        }
    }

    # Basic 
    headers = {
        "Authorization": "Basic Y2Rvc29yaW9iOmNodXdld2U="
    }

    sheety_endpoint = "https://api.sheety.co/9a58efae000087421425a9fd22e83a95/workoutTracking/workouts"

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=headers)
    sheety_response.raise_for_status()
    print(sheety_response.text)