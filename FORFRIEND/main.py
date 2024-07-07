import subprocess
import requests
import os
from data import quote

FRIEND_NUMBER = os.environ.get("FRIENDNUMBER")
API_KEY=os.environ.get("APIKEY")
MY_LAT = 3.139003
MY_LONG= 101.686852
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt":4,
}

response = requests.get(url = API_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
will_sun = True
message = ""
for hour_data in data["list"]:
    code = hour_data["weather"][0]["id"]
    if int(code) < 800:
        will_rain = True
    else:
        will_sun = True

if will_rain:
    message = f"Hey Cloudi☁️! Don't forget to bring an umbrella☔️\n\n---*{quote}*--- \n Let grab a coffee ☕️\n\nFrom Sunny🌞"
if will_sun:
    message = f"Hey Cloudi☁️! Stay calm and drink water🥤 enough\n\n---*{quote}*--- \n Let grab a coffee ☕️\n\nFrom Sunny🌞"

def send_imessage(phone_number, message):
    applescript = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript])

send_imessage(FRIEND_NUMBER, message)
# message = f"Hey Cloudi! Don't forget to bring an umbrella☔️\n\"{quote}\"\nFrom Sunny"
# print(message)
