from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

import requests

CLIENT_ID = "8ee283f496b64bc99e56ed35eba229cc"
CLIENT_SECRET = "7ff999a6926d4a5285856d89d035cb30"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://cowboy-clone-ten.vercel.app",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Jamal", 
    )
)

user_id = sp.current_user()["id"]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")



response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")


# scraping the song titles
soup = BeautifulSoup(response.text, "html.parser")
song_names_span = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_span]



song_uris = []

year = date.split('-')[0]
for song in song_names:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped!")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)