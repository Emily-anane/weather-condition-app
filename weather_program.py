import requests

api_key = "d2f8b3c6e0c1ff567922995b1d9ce5a1"

user_input = input("Enter your city:  ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
)
if weather_data.json()['cod'] == '404':
    print ("No city found")
else: 
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is {weather}")
    print(f"The temperature in {user_input} is {temp}")