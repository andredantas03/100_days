import re
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv("../.env")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/example",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Andre Dantas",
    )
)
user_id = sp.current_user()["id"]




while True:
    # date = input("Which year do you want  to travel to? Type the date in this format: YYYY-MM-DD")
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
    date = '2010-10-10'
    if re.fullmatch(pattern, date):
        print("Data válida")
        break
    else:
        print("Data inválida")

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'}

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}', headers = header)

soup = BeautifulSoup(response.text,'html.parser')

songs = soup.select('li ul li h3')
song_titles = []
for song_title in songs[:10]:
    song_titles.append(song_title.getText().strip())


year = date.split('-')[0]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(song_uris)
playlist = sp.user_playlist_create(user = user_id,
                             name = f"Playlist from date: {date}",
                             description= f"Playlist Created by webscrapping date: {date}",
                             public=False)

action_add_tracks = sp.playlist_add_items(playlist_id = playlist['id'],
                                          items = song_uris)

print(action_add_tracks)