import pandas as pd


def get_artist(sp, artist_name, index=0):
    
    artist = (
        sp.search(artist_name, type='artist')
        ['artists']
        ['items'][index]
    )
    
    artist_list = get_artist_dict(artist)
    
    return artist_list, artist_list['genres']

def get_artist_dict(artist):
    return {
        'artist_uri': artist['uri'],
        'name': artist['name'],
        'genres': artist['genres'],
        'popularity': artist['popularity'],
        'followers': artist['followers']['total'],
    }

def get_artist_albums(sp, artist_uri):
    return sp.artist_albums(artist_uri)['items']

def get_album_dict(album):
    return {
        'album_uri': album['uri'],
        'album_type': album['album_type'], 
        'type': album['type'], 
        'name': album['name'], 
        'total_tracks': album['total_tracks'], 
        'release_date': album['release_date'], 
    }

def get_tracks_dict(sp, album_uri):
    album_tracks = sp.album_tracks(album_uri)['items']
    return [
        {
            'album_uri': album_uri,
            'track_uri': track['uri'], 
            'number': track['track_number'], 
            'name': track['name'], 
            'duration_ms': track['duration_ms'], 
            'explicit': track['explicit'], 
            'preview_url': track['preview_url']
        }
        for track in album_tracks
    ]

def init(sp, artist_name, index=0):
    
    artist = (
        sp.search(artist_name, type='artist')
        ['artists']
        ['items'][index]
    )
    
    artist_list = get_artist_dict(artist)
    
    return artist_list, artist_list['genres']

def get_tracks_features(sp, tracks):
    return [sp.audio_features(t['track_uri'])[0] for t in tracks]

def get_clear_tracks_features(sp, tracks):
        
    return (pd
        .DataFrame(get_tracks_features(sp, tracks))
        .drop(['type', 'id', 'track_href', 'analysis_url', 'duration_ms'], axis=1) 
        .rename({'uri': 'track_uri'}, axis=1)
    )

def get_track_analysis(sp, track_uri):

    track_analysis = sp.audio_analysis(track_uri)['track']

    track_analysis['track_uri'] = track_uri
    track_analysis.pop('codestring')
    track_analysis.pop('code_version')
    track_analysis.pop('echoprintstring')
    track_analysis.pop('echoprint_version')
    track_analysis.pop('synchstring')
    track_analysis.pop('synch_version')
    track_analysis.pop('rhythmstring')
    track_analysis.pop('rhythm_version')
    
    return track_analysis

def get_tracks_analysis_dict(sp, tracks):
    
    return [get_track_analysis(sp, t['track_uri']) for t in tracks]

def get_clear_tracks_analysis(tracks):
    pass

def get_tracks_series(sp, tracks, series_type='beats'):

    """
    Returns a DataFrame containing the time series data for the given tracks.

    Args:
        tracks: A list of dictionaries, where each dictionary represents a track and contains a 'track_uri' key.
        series_type: {“beats”, “bars”, “tatums”, “sections“, “segments“}, default=”beats”.

    Returns:
        A DataFrame containing the time series data for the given tracks.
        
    """

    tracks_series = []

    for t in tracks:

        series = pd.DataFrame(
            sp.audio_analysis(t['track_uri'])[series_type]
        )

        series['track_uri'] = t['track_uri']

        tracks_series.append(series.copy())

    return (pd
        .concat(tracks_series)
        .reset_index()
        .rename({'index': 'track_index'}, axis=1)
    )

def pipeline_By_genre(sp, artist_name):

    artist_list, genres = init(artist_name)

    for genre in genres:

        print(f'fetching {genre}')

        offset = 0

        while True:

            results = (
                sp.search(q='genre:' + genre, type='artist', offset=offset)
                ['artists']
                ['items']
            )

            if results:

                artist_list += [get_artist_dict(artist) for artist in results]

                new_genres = set(sum([get_artist_dict(artist)['genres'] for artist in results], []))
                genres += [g for g in new_genres if g not in genres]

                offset = len(results)

            else:
                print(f' | Total bands: {offset}')
                break
                
    return artist_list

def get_all_tracks_features(sp, artist_uri):
    
    albums = get_artist_albums(sp, artist_uri)
    df_albums = (pd
        .DataFrame([get_album_dict(album) for album in albums])
        .rename({'name': 'album_name'}, axis=1)
    )
    
    track_list = []
    for uri in df_albums.album_uri:
        tracks = get_tracks_dict(sp, uri)
        tracks_features = get_clear_tracks_features(sp, tracks)
        df_tracks = (pd
            .DataFrame(tracks)
            .merge(tracks_features, on='track_uri', how='left')
            .rename({'name': 'track_name'}, axis=1)
        )
        track_list.append(df_tracks.copy())
    df_all_tracks = pd.concat(track_list)
    
    return df_albums.merge(df_all_tracks, on='album_uri', how='inner') 