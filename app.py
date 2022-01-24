import requests

# Get Free API HERE: https://openweathermap.org/

API = 'INESRT YOUR API KEY HERE'
CITY=input("Enter City Name: ")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

url = f"{BASE_URL}?q={CITY}&appid={API}"

response = requests.get(url)

if response.status_code==200:
    data = response.json()
    longitude = data['coord']['lon']
    latitude = data['coord']['lat']
    weather = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15
    min_temperature = data['main']['temp_min'] - 273.15
    max_temperature = data['main']['temp_max'] - 273.15
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    visibility = data['visibility']
    wind_speed = data['wind']['speed']
    wind_direction = data['wind']['deg']
    clouds = data['clouds']['all']
    country = data['sys']['country']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")
    print(f"Weather: {weather}")
    print(f"Temparature: {round(temperature,2)} Celcius")
    print(f"Minimum Temparature: {round(min_temperature,2)} Celcius")
    print(f"Maximum Temparature: {round(max_temperature,2)} Celcius")
    print(f"Pressure : {pressure}")
    print(f"Humidity: {humidity}")
    print(f"Visibilty: {visibility}")
    print(f"Wind Speed: {wind_speed} M/s")
    print(f"Wind Direction: {wind_direction}")
    print(f"Clouds: {clouds} %")
    print(f"Country: {country}")
    print(f"Sunrise: {sunrise} UTC")
    print(f"Sunset: {sunset} UTC")

else:
    print("API Error")
