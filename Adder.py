import requests
import auth
import SoundFinder
#* Add songs from a selected playlist
for song in SoundFinder.id_song:
    post = requests.post(f'https://api.deezer.com/playlist/7830522482/tracks?songs={song}&request_method=post&access_token={auth.access_token}')