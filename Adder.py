import requests
import auth
import SoundFinder
import edit_me
#* Add songs from a selected playlist
def Add():
    with open('songs_id.txt', 'r') as f:
        songs = f.read().splitlines()
        for song in songs:
            post = requests.post(f'https://api.deezer.com/playlist/{edit_me.deezer_playlist}/tracks?songs={song}&request_method=post&access_token={auth.access_token}')