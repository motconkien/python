import requests
from bs4 import BeautifulSoup
import spotipy
import json


#web scrapping
prompt = input("Which year do you want to travel to? Type the dte in this format YYYY-MM-DD\n")
URL = f"https://www.billboard.com/charts/hot-100/{prompt}/" 
#igest raw data
response = requests.get(url=URL)
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
songs = soup.select("li ul li h3")
songs_name = []
for song in songs:
    songs_name.append(song.getText().strip())

#spotify
CLIENT_ID = "610535ef9e484917aaaf1a93fd4d5bcd"
CLIENT_SECRET = "82e08828ebe54264be46cf8929d901e8"
REDIRECT_URL = "http://example.com"

with open("Day46/token.json", "r") as file:
    data = json.load(file)
# print(data)

# sp = spotipy.Spotify(
#     auth_manager=spotipy.SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="Day46/token.json",
#     )
# )
sp = spotipy.Spotify(auth=data["access_token"], requests_session=True)
user_id = sp.current_user()['id']
# print(user_id['id'])
# print(songs_name)
list_songs = []
year = prompt.split("-")[0]
for song in songs_name:
    result = sp.search(
        q=f"track:{song} year:{year}",  # Added year to the query
        type='track'
    )
    try:
        uri = result["tracks"]["items"][0]["uri"]
        list_songs.append(uri)
    except IndexError:
        print(f"{song} doesnt exist in Spotify. skipped")
playlist = sp.user_playlist_create(user = user_id,name = f"{prompt} Billboard100",public=False)
print(playlist)
try: 
    sp.playlist_add_items(playlist["id"],items = list_songs)
except spotipy.exceptions.SpotifyException as e:
    print("Error: ",e)
    
