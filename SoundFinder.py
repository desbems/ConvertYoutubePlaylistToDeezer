import requests

#TODO: Remove videos.txt after use
#TODO: Create a log file with datetime
#TODO: Ability to choose playlist
with open('log.txt', 'a') as log:
    with open('videos.txt', 'r') as f:
        te = f.read().splitlines()
        artist_name = []
        song_name = []
        result = []
        id_song = []
        #* split name and add the artist name 
        for names in te:
            split = names.split("-")
            if len(split) == 2:
                artist_name.append(split[0])
                d = split[1].strip()
                song_name.append(d)
        print(artist_name)
        print(song_name)
#FIXME: If song is present two times, remove one
        for name in artist_name:
                get = requests.get(f'https://api.deezer.com/search?q={name}&output=json')
                liste = get.json()
        #* print every song name found on DEEZER database
                for t in liste['data']:
                    bang = t['title']
                    for song in song_name:
                        if song == bang:
                            log.write(song + " : ID found")
                            log.write("\n")
                            id_song.append(t['id'])
                            break
                        else:
                            pass
        
        print(id_song)
