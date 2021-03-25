import SoundFinder
import youtubeLikedPlaylist
import youtubePlaylist
import Adder

choice = input("Choice : ")
if choice == "1":
    youtubeLikedPlaylist.Liked()
    Adder.Add()
else :
    youtubePlaylist.Playlist()
    Adder.Add()

