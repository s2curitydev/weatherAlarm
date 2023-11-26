import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = os.environ.get("OWM_API_KEY=")

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_parameter = {
    "lat": 49.499138,
    "lon": -119.593704,
    "appid": api_key,
    "lang": "kr",
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
twelve_hourly_data = weather_data["hourly"][:12]

will_rain = False

for hour in twelve_hourly_data:
    if hour["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="This is weather AI created by Han. <<NOTE>> It's going to be rain today. Remember to bring an ☂️",
            from_='+19498607327',
            to='+17789547942'
        )
    print(message.status)

print(">> Run <<")
