import requests
import webbrowser
import edit_me
#* open browser to get the token
url = webbrowser.open(f'https://connect.deezer.com/oauth/auth.php?app_id={edit_me.deezer_id}&redirect_uri=https://google.com&perms=manage_library,email')
token = input('Enter the token : ') #token is in the url : "e : https://www.google.com/?code=*(frdc4a91c6b95f0f6b6e46aa4720275a)*"
url2 = requests.get(f'https://connect.deezer.com/oauth/access_token.php?app_id={edit_me.deezer_id}&secret={edit_me.deezer_key}&code={token}&output=json')
#* return the authentifcation token
accessToken = url2.json()
access_token = accessToken['access_token']
