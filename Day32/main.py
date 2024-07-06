import smtplib
from datetime import datetime
import pandas as pd
import random

MY_EMAIL = "hoanghuyen.hh20897@gmail.com"
PASSWORD = "pass" #need to change to accurate password when using

mon = datetime.now().month
date = datetime.now().day
today = (mon,date)
# print(today)

df = pd.read_csv("Day32/birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row 
                 for (index, data_row) in df.iterrows()
                 }
# print(birthday_dict)
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"Day32/letters_template/letter_{random.randint(1,3)}.txt"
    print(f"Attempting to send letter to {birthday_person['name']} at {birthday_person['email']}")

    try:
        with open(file_path) as letter:
            content = letter.read()
            content = content.replace("[NAME]", birthday_person["name"])
            # print(content)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject: Happy Birthday!\n\n{content}"
            )
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTPException: {e}")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Email sent successfully.")