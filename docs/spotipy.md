# Spotipy features
___
### Track
#### Raw features
- **EXPLICIT** - Refers to whether a track contains explicit lyrics. It is typically represented as a boolean value, where a value of true indicates that the track contains explicit lyrics and a value of false indicates that the track does not contain explicit lyrics.

- **DURATION_MS** - Refers to the duration of a track. It is typically represented as the number of milliseconds that the track lasts.

- **KEY** - Refers to the tonality of a track. Specifically, it refers to the pitch class of the tonic note (which is the note around which a piece of music is centered). The key of a track is typically represented as a number from 0 to 11.

    Where: **0** represents the key of C, **1** represents the key of C♯/D♭, **2** represents the key of D, and so on.
    
- **MODE** - Refers to the tonality of a track. Specifically, it refers to whether a track is in a major key or a minor key.

    Where: **0** Minor or **1** Major.
    
- **TIME_SIGNATURE** - refers to the time signature of a track.
    
- **TEMPO** - Refers to the speed of a track. It is typically represented in beats per minute (BPM), which is a measure of how many beats occur in one minute of music.
    
- **LOUDNESS** - Refers to the volume level of a track. It is typically represented in decibels (dB) relative to full scale. Full scale is the maximum possible volume level that a track can have, and it is represented as 0 dB. 

    **Ex:** A track with a loudness level of -10 dB is 10 dB quieter than full scale, while a track with a loudness level of +5 dB is 5 dB louder than full scale.

#### Audio features that the Spotify Web API provides for tracks
- **ENERGY** - Refers to the intensity and activity level of a track. It is typically represented on a scale from 0 to 1.

    Where: **0** indicates that a track is low in energy and **1** indicates that a track is high in energy.
    
    Profile: 
    
    Tracks that are high in energy tend to have a fast tempo, a strong beat, and a high volume level. They may also have a high level of danceability and a positive valence (perceived positivity).

- **DANCEABILLIY** - Refers to the likelihood that a track will inspire people to dance. It is typically represented on a scale from 0 to 1

    Where: **0** indicates that a track is unlikely to inspire dancing and **1** indicates that a track is highly likely to inspire dancing.
    
    Profile: 
    
    Tracks that are highly danceable tend to have a fast tempo, a steady beat, and a repetitive structure. They may also have a high level of energy and a positive valence (perceived positivity).

- **INSTRUMENTALNESS** - Refers to the likelihood that a track contains no vocals. It is typically represented on a scale from 0 to 1.

    Where: **0** indicates that a track is highly likely to contain vocals and **1** indicates that a track is highly likely to be instrumental.
    
    Profile: 
    
    Tracks that are purely instrumental, with no vocals, can be useful for certain purposes such as background music or studying.
    
- **SPEECHINESS** - Refers to the likelihood that a track contains spoken words. It is typically represented on a scale from 0 to 1.

    Where: **0** indicates that a track is highly unlikely to contain spoken words and **1** indicates that a track is highly likely to contain spoken words.
    
    Profile: 
    
    Tracks that contain spoken words, such as podcasts or audiobooks, can be useful for certain purposes such as learning or entertainment. 

- **LIVENESS** - Refers to the likelihood that a track was recorded in front of a live audience. It is typically represented on a scale from 0 to 1.

    Where: **0** indicates that a track is highly likely to be a studio recording and **1** indicates that a track is highly likely to have been recorded live.
    
    Profile: 
    
    Tracks that are recorded live tend to have a different sound and feel compared to studio recordings. They may have a higher level of energy and a more spontaneous or raw quality, as they are typically performed in front of an audience in real-time. 
    
- **ACOUSTICNESS** -  Refers to the likelihood that a track was recorded using primarily acoustic instruments. It is typically represented on a scale from 0 to 1.

    Where:  **0** indicates that a track is highly likely to be electronic or amplified and **1** indicates that a track is highly likely to be acoustic.
    
    Profile:
    
    Tracks that are highly acoustic tend to have a natural, organic sound, as they are typically recorded using instruments such as guitars, pianos, and drums that are played without the use of electronic amplification.

- **VALENCE** - Refers to the perceived positivity or negativity of a piece of music. It is typically represented on a scale from 0 to 1.

    Where: **0** is extremely negative and **1** is extremely positive.
    
    Profile: 
    
    For example, a track with a high valence rating might be described as upbeat, cheerful, or happy, while a track with a low valence rating might be described as sad, melancholy, or downbeat.