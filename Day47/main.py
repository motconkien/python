from bs4 import BeautifulSoup
import requests
import os
import smtplib

email = os.environ.get("email")
password = os.environ.get("pass")


URL = "https://www.amazon.com/nuphy-Portable-Mechanical-Compatible-Bluetooth/dp/B0CQRL2CDV/ref=sr_1_8?crid=AC9ROCYRUSU2&dib=eyJ2IjoiMSJ9.k7VYBM4zFjwhCn-yA8ZKSVEGUH7wYbVgTJqi7rJPSbUhZc5bFoDGguvyFasOYLFoo0TKgMCW6gYw22Bqb_4KSk5OdhuSA8YzUln3K71V4j7psvnCVzJOvyyCseP1lZzrHPijuaZrU2wmbN69Best4j0jnJyw9dKRIj2nMyXkXBIZc0nmlwwg27JUD3JFHqS4YkUSJU4T2To-dnr05MU-kRuo7G3VlkePqGMjHbYquEI.GQ9MwYrFk6EpvnvWaJb9_1ctBkXehuSML0d5tcD2sGM&dib_tag=se&keywords=keyboard+nuphy&qid=1721397255&sprefix=keyboard+nu%2Caps%2C300&sr=8-8"
header = {
    "Accept-Language":"en-US,en;q=0.9",
}
response = requests.get(URL, headers=header)
data = response.content

soup = BeautifulSoup(data,"html.parser")
# print(soup.prettify())
price_symbol = soup.find(class_='a-offscreen')
if price_symbol:
    price = price_symbol.get_text().lstrip("$")
    if float(price) < 150:
        message = f"Price for Nuphy keyboard is {price}"
        with smtplib.SMTP("smtp.gmail.com",port = 587) as con:
            con.starttls()
            con.login(email,password)
            con.sendmail(from_addr=email,to_addrs="hynuiux@gmail.com",msg=message)
            print("Send successfully")