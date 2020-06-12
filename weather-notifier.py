import re
import requests
import os

def send_sms(phone_number, message):
    account_sid = os.environ['ACCOUNT_SID']
    token = os.environ['TOKEN']
    from_number = os.environ['FROM_NUMBER']
    twilio_sms_api_url = f'https://{account_sid}:{token}@api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    parameters = {'From': from_number, 'To': phone_number, 'Body': message}
    response = requests.post(twilio_sms_api_url, data=parameters).json()
    return response

def check_if_12(forecast_dictionary):
    match = re.search(r'12:00:00', forecast_dictionary['dt_txt'])

    if match:
      return True
    else:
      return False

def check_if_3(forecast_dictionary):
    match = re.search(r'03:00:00', forecast_dictionary['dt_txt'])

    if match:
      return True
    else:
      return False

def stringify_forecast(forecast_pair):
    temperature_night = round(forecast_pair[0]['main']['temp'])
    temperature_day = round(forecast_pair[1]['main']['temp'])
    weather_description = forecast_pair[1]['weather'][0]['description']
    cloudiness = forecast_pair[1]['clouds']['all']
    date = forecast_pair[1]['dt_txt'].split(' ')[0]
    return f"Weather for {city} on {date}:\n🌡️️: {temperature_night}°C night / {temperature_day}°C day\n🌤️: {weather_description}\n☁️: {cloudiness}%\n"

city = os.environ['CITY']
app_id = os.environ['APP_ID']
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={app_id}&units=metric'

forecasts = requests.get(url).json()
choose_12 = list(filter(check_if_12, forecasts['list']))
choose_3 = list(filter(check_if_3, forecasts['list']))
forecast_pairs = list(zip(choose_3, choose_12))

message = ''

for forecast_pair in forecast_pairs:
    message += stringify_forecast(forecast_pair)

send_sms(os.environ['TO_NUMBER'], message)
