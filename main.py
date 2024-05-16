import requests
from twilio.rest import Client

api_key = "c79d06264d25e466669b44cfb7c65e86"
MY_LAT = 41.203980
MY_LONG = 33.555470
account_sid = "*****"
auth_token = "*****"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

# print(response.status_code)
# print(response)

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
weather_ids = []

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella. ☔︎",
        from_="+16504899389",
        to="+905369910917"
    )
    print(message.status)