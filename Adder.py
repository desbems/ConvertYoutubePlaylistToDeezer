import requests
import auth
import SoundFinder
import edit_me
#* Add songs from a selected playlist

for song in SoundFinder.id_song:
    post = requests.post(f'https://api.deezer.com/playlist/{edit_me.deezer_playlist}/tracks?songs={song}&request_method=post&access_token={auth.access_token}')