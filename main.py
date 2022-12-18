import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "Your API Generated KEY from open weather"

account_sid = "your sid from twilio"
auth_token = "your token"

weather_params = {
    "lat": 17.440081,
    "lon": 78.348915,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to be rain today, Remember to bring an ☂.",
        from_='your twilio number',
        to='number you want to send message'
    )

    print(message.status)
