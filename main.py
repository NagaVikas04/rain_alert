import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "48447110125b1ca4dcbe157e030bd5de"

account_sid = "ACd51b6ff564315082e4670dbeb2d7b14f"
auth_token = "bc5c3d378590d361c8e0b9e1b00bbfec"

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
        from_='+13862604649',
        to='+917997665598'
    )

    print(message.status)
