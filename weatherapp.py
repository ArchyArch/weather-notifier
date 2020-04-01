import requests

city = input('City name: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=767573953473bdb871a80111df8b19af&units=metric'

json_data = requests.get(url).json()
formatted_data = json_data['main']['temp']
formatted_data1 = json_data['weather'][0]['description']
print(f'Temperature: {formatted_data}' + '°C, Weather: ' + formatted_data1)
