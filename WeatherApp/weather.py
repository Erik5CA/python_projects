import re
from apikey import API_KEY
from requests import get

URL = 'http://api.openweathermap.org/geo/1.0/direct'

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_lat_long(city):
    request_url = f'{URL}?q={city}&limit=4&appid={API_KEY}'
    
    response = get(request_url, timeout=5)
    
    if response.status_code == 200:
        data = response.json()
        if len(data) != 0:
            data = data[0]
            city = data['name']
            lat = data['lat']
            lon = data['lon']
            print(f'{city}')
            return lat, lon
        else:
            print('Not found results for this search.')
            return None, None
    else:
        print('Error')
        return None, None
    

def get_weather(lat, lon):
    request_url = f'{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}'

    response = get(request_url, timeout=5)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        print(f'Weather: {weather}')
        print(f'Temperature: {temperature} °C')
    else:
        print('Error')

def main():
    city = input('Enter a city name: ')
    lat, lon = get_lat_long(city)
    if lat is not None and lon is not None:
        get_weather(lat, lon)
    

main()
    