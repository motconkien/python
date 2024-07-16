import requests
from bs4 import BeautifulSoup


# prompt = input("Which year do you want to travel to? Type the dte in this format YYYY-MM-DD")
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

#igest raw data
response = requests.get(url=URL)
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
songs = soup.select("li ul li h3")
songs_name = []
for song in songs:
    songs_name.append(song.getText().strip())
