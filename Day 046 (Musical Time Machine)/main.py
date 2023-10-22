#Musical Time Machine Project
######################################################
from bs4 import BeautifulSoup
import requests

date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD \n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, 'html.parser')

#Using the select method to find all of the h3 elments inside li elements that are inside ul elements that are inside li elements
song_names_spans = soup.select("li ul li h3")

#using list comprehension to get the text from each span element and strip the whitespace
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

######################################################
#Spotify API access and authentication
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from api_key import spotify_id, spotify_secret, sp_username

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_id,
        client_secret=spotify_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=sp_username, 
    )
)
user_id = sp.current_user()["id"]

######################################################
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

######################################################
        sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_id,
        client_secret= spotify_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)