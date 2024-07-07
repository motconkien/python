import requests
import smtplib
import os

MY_EMAIL = "hoanghuyen.hh20897@gmail.com"
PASSWORD = os.environ.get("PASSWORD")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Telsa Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_KEY = os.environ.get("APIKEY")
NEWS_API_KEY = os.environ.get("NEWAPI")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(url = STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value)in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

day_before_yesterday = data_list[1]
day_before_closing_price = yesterday_data['4. close']
print(day_before_closing_price)

difference_price = float(yesterday_closing_price) - float(day_before_closing_price)
up_down = ""
if difference_price > 0:
    up_down = "🔺"
else:
    up_down =  "🔻"
print(difference_price)

diff_percent = round((difference_price/float(yesterday_closing_price) )*100,2)

three_articles=[]
get_new = False
if abs(diff_percent) >= 5:
    new_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    new_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = new_response.json()["articles"]
    three_articles = articles[:3]
    get_new = True


if get_new:
    formatted_articles = [f"Subject: {STOCK_NAME}: {up_down}{up_down}% {article["title"]} \n\n Brief: {article['desciption']}" for article in three_articles]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        for article in formatted_articles:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg= article
                )