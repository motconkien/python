import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "hoanghuyen.hh20897@gmail.com"
PASSWORD = "pass"

MY_LAT = 35.689487
MY_LONG = 139.691711

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org//iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }

    API_link = "https://api.sunrise-sunset.org/json"
    response = requests.get(API_link, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrine = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrine:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead and is_night:
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look up \n\n The ISS is above you in the sky."
            )