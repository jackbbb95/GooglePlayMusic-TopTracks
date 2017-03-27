from gmusicapi import Mobileclient
from config import *

#API
api = Mobileclient()
logged_in = api.login(gpm_username, gpm_password, '1234567890abcdef')

#Data
artist_id_dict = {}
desired_playlist_id = ''
all_song_ids = []

#Retreive the playlist id from api based on name in config.py
def get_playlist_id():
    all_playlists = api.get_all_playlists(False, None)
    for playlist in all_playlists:
        if (playlist['name'] == output_playlist):
            return playlist['id']

#Retreive artist ids from api based on list in config.py
def get_artist_ids():
    ids = {}
    for artist in artists_list:
        query_results = api.search(artist,1)
        artist_id = query_results['artist_hits'][0]['artist']['artistId']
        ids[artist] = artist_id
    return ids

#gathers the ids of top tracks from each artist. amount_of_tracks in config.py for #
def get_top_tracks():
    song_ids = []
    for artist in artist_id_dict:
        query_results = api.get_artist_info(artist_id_dict[artist],False,amount_of_tracks,0)
        try:
            top_tracks = query_results['topTracks']
        except Exception as e:
            print('Artist ' + query_results['name'] + ' has no top tracks listed')
            pass

        for track in top_tracks:
            song_ids.append(track['storeId'])
    return song_ids

if (logged_in):
    desired_playlist_id = get_playlist_id()
    print('done locating playlist')

    artist_id_dict = get_artist_ids()
    print('done gathering artists')

    all_song_ids = get_top_tracks()
    print('done finding top tracks')

    api.add_songs_to_playlist(desired_playlist_id, all_song_ids)
    print('done adding top tracks to playlist!')
else:
    print('Please provide login credentials in config.py')
