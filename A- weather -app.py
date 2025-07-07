import requests

city_name="Accra"

API_KEY="7b33bc7a8ef8e73bf9d2a1a42d7304b9"
The_weather =requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={ API_KEY}")



weather_condition=The_weather.json()
print(weather_condition)


temperature=weather_condition ["main"]["temp"]

if temperature <=300.38:
    print(f"The weather is warm ")


else:
    print(F"The weather is hot ")