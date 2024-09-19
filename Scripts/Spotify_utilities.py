import re
from requests import get
from Getting_access_to_SpotifyAPI import get_auth_header

def clean_characters(string):
    return re.sub(r'[^a-zA-Z0-9\u3040-\u30FF\u4E00-\u9FFF\u1100-\u11FF\u3130-\u318F\uAC00-\uD7AF\u0400-\u04FF\s]','',string)

def search_for_artist(token, artistName, limit, clean):
    if clean==True:
        artistName = clean_characters(artistName) 
    url = "https://api.spotify.com/v1/search" + "?" + f"q={artistName}&type=artist&limit={limit}"
    result = get(url, headers=get_auth_header(token))
    result = result.json()["artists"]["items"]
    
    return result

def get_all_results_artist(token, artistName):
    all_results = []
    url = "https://api.spotify.com/v1/search" + "?" + f"q={artistName}&type=artist&limit=50"
    
    while url:
        result = get(url, headers=get_auth_header(token))
        data = result.json()
        all_results.extend(data["artists"]["items"])               
        url = data.get("next")
    
    return all_results

def search_for_song(token, songName, limit, clean):
    if clean==True:
        songName = clean_characters(songName)   
    url = "https://api.spotify.com/v1/search"
    query = url + "?" + f"q={songName}&type=track&limit={limit}"
    result = get(query, headers=get_auth_header(token))
    result = result.json()['tracks']['items']
            
    return result

def get_all_results_songs(token, songName):
    all_results = []
    url = "https://api.spotify.com/v1/search" + "?" + f"q={songName}&type=track&limit=50"
    
    while url: #This loop works while results are up. Otherwise, this gives None
        result = get(url, headers=get_auth_header(token))
        data = result.json()      
        all_results.extend(data["tracks"]["items"])               
        url = data.get("next")
    
    return all_results

def get_top_tracks_from_artist(token, artistID, market):
    url = f'https://api.spotify.com/v1/artists/{artistID}/top-tracks'+f'?market={market}'
    result = get(url, headers=get_auth_header(token))
    result = result.json()["tracks"]
    
    return result
    
def get_albums_from_artist(token, artistID):
    limit = 50
    offset = 0
    all_albums = []
    
    while True: 
        url = f'https://api.spotify.com/v1/artists/{artistID}/albums?limit={limit}&offset={offset}'
        result = get(url, headers=get_auth_header(token))

        if result.status_code == 200: #A succeded result
            current_albums = result.json()["items"]
            all_albums.extend(current_albums)

            if len(current_albums) < limit:
                break
            else:
                offset += limit

    return all_albums

def get_album_tracks(token, albumID):
    url = f'https://api.spotify.com/v1/albums/{albumID}/tracks'
    result = get(url, headers=get_auth_header(token))
    result = result.json()["items"]
    
    return result

def get_track(token, trackid):
    url = f'https://api.spotify.com/v1/tracks/{trackid}'
    result = get(url, headers=get_auth_header(token))
    result = result.json()
    
    return result

def  get_several_info(token, type_of_data, ids):    
    if type_of_data not in ['tracks', 'audio-features', 'albums', 'artists']:
        raise ValueError('Opcion no valida')
    
    ids_conc = ''
    for i in ids:
        ids_conc = ids_conc+i+','
    ids_conc = ids_conc[:len(ids_conc)-1]
    
    url = f'https://api.spotify.com/v1/{type_of_data}?ids={ids_conc}'
    if type_of_data=='audio-features':
        type_of_data = 'audio_features'
    result = get(url, headers=get_auth_header(token))
    result = result.json()[type_of_data]
    
    return result