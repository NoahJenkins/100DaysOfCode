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
from api_key import spotify_id, spotify_secret

#Spotify API access and authentication
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from api_key import spotify_id, spotify_secret, username


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=spotify_id
        client_secret= spotify_secret
        show_dialog=True,
        cache_path="token.txt",
        username=username
    )
)
user_id = sp.current_user()["id"]