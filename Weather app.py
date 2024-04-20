import requests
import json
import pyttsx3
city=input("Enter the name of the city\n")
url=f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"
r=requests.get(url)
print(r.text)
weather_dic=json.loads(r.text)
print(weather_dic["current"]["temp_c"])
w=weather_dic["current"]["temp_c"]
robo=pyttsx3.init()
robo.say(f"the weather of {city} is {w}")
robo.runAndWait()
