# weather-notifier

A simple weather notifier using Twilio and OpenWeaterMap API and including city, temperature in °C for night (3:00 AM) and day (12:00 PM), weather description and cloudiness in %.

### How to use it?

1. Download my script.
2. Use environmental variables: ACCOUNT_SID (from Twilio), TOKEN (from Twilio), FROM_NUMBER (from Twilio), TO_NUMBER (your number), CITY (your city), APP_ID (from OpenWeatherMap) 
3. Run the script in terminal -> `python weather-notifier.py`
4. A weather for the nearest 5 days will be sent to your phone.

