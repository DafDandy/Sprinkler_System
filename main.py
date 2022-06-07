# importing modules
import requests, json

# API base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# City Name
CITY = "Royal Oak"

# Your API key
API_KEY = "5b9a9ee80ff58a71a11b6e95ca407c07"

# updating the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

# Sending HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
    
   # retrieving data in the json format
   data = response.json()
   
   # take the main dict block
   main = data['main']
   
   # getting temperature
   temperature = round(int(main['temp']) * 9/5 - 459.67, 0)
   # getting feel like
   temp_feel_like = round(int(main['feels_like']) * 9/5 - 459.67, 0)
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   
   # weather report
   weather_report = data['weather']
   # wind report
   wind_report = data['wind']
   
if temperature > 55:
    print('ok')

 if pressure < 1:
    print('ok')


#    print(f"{CITY:-^35}")
#    print(f"City ID: {data['id']}")   
#    print(f"Temperature: {temperature}")
#    print(f"Feel Like: {temp_feel_like}")    
#    print(f"Humidity: {humidity}")
#    print(f"Pressure: {pressure}")
#    print(f"Weather Report: {weather_report[0]['description']}")
#    print(f"Wind Speed: {wind_report['speed']}")
# else:
#    # showing the error message
#    print("Error in the HTTP request")
