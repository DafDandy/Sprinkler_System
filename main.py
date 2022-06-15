import requests, json, os
from re import search
import time

def weather_api():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Ferndale"
    API_KEY = '5b9a9ee80ff58a71a11b6e95ca407c07'
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = round(int(main['temp']) * 9/5 - 459.67, 0)
       temp_feel_like = round(int(main['feels_like']) * 9/5 - 459.67, 0)
       humidity = main['humidity']
       pressure = main['pressure']
       weather_report = data['weather']
       wind_report = data['wind']
    if temperature > 55:
        print(f"{CITY:-^35}")
        print(f"City ID: {data['id']}")   
        print(f"Temperature: {temperature}")
        print(f"Feel Like: {temp_feel_like}")    
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {weather_report[0]['description']}")
        print(f"Wind Speed: {wind_report['speed']}")
    else:
        print("Error in the HTTP request")
        
from bs4 import BeautifulSoup
import datetime, time

rain = 'rain'
thunderstorm = 'thunderstorm'

def time_check():
    now = datetime.datetime.now()
    today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
    today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
    if now > today8am and now < today9am:
        print('test complete')
    else:
        print('sleeping')
        time.sleep(10)

def sprinkler_check():   
    url='https://www.yahoo.com/news/weather/?guccounter=1'
    page = requests.get(url)
    soup =  BeautifulSoup(page.content,'html.parser')
    text = soup.get_text()
    f = text.split('-')
    c = f[3]
    forecast = c.split('. ')
    current_day = forecast[0]
    current_night = forecast[2]
    if rain in current_day:
        pass
    if thunderstorm in current_day:
        pass
    if rain or thunderstorm not in current_day:
        print('turn on')