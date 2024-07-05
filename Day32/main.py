import smtplib
from datetime import datetime
import pandas as pd
import random

MY_EMAIL = "hoanghuyen.hh20897@gmail.com"
PASSWORD = "huyen20897"

today = (datetime.now().month, datetime.now().day)
print(today)
df = pd.read_csv("Day32/birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Day32/letters_template/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("sptm.gamil.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=birthday_person["email"],
                            MSG = f"Subject: Happy Birthday!\n\n {content}")