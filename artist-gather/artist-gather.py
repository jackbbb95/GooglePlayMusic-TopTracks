from gmusicapi import Mobileclient
from config import *

# API
api = Mobileclient()
logged_in = api.login(gpm_username, gpm_password, '3a6a9d34f7e8237e')

# Data
artist_names = []

for song in api.get_all_songs():
    artist = song['artist']
    if not(any(artist[:5].lower() in n.lower() for n in artist_names)):
        artist_names.append(artist)

artist_names.sort()

file = open("artist.txt","w")
for artist in artist_names:
    print(artist)
    file.write(artist + "\n")
file.close()
