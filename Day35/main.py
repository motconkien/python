import requests
import smtplib
import os 

MY_EMAIL = "hoanghuyen.hh20897@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

api_key = os.environ.get("MY_API")
MY_LAT = 35.689487
MY_LONG = 139.691711
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt":4,
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
will_sun = False
message = ""
for hour_data in weather_data["list"]:
    code = hour_data["weather"][0]["id"]
    if int(code) < 800:
        will_rain = True
    else:
        will_sun = True

if will_sun:
    message = "Bring your hat and water"
if will_rain:
    message = "Bring your an umbrella"

if will_rain or will_sun:
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject: Remind \n\n {message}"
        )

