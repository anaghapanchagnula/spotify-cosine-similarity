import spotipy
from spotipy.oauth2 import SpotifyOAuth
import math 

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
  client_id='c6612c035d594fc29de26e400b845759',
  client_secret='993c5c137511405983d1f7381f1aa807',
  redirect_uri='http://localhost:5000/callback',
  scope='user-top-read'
))

def extractFeatures(features): 
  return [
    features['danceability'],
    features['energy'],
    features['key'],
    features['speechiness'],
    features['acousticness'],
    features['instrumentalness'],
    features['valence'],
  ]

def searchSong(sp, songName, artistName):
    query = f"track:{songName} artist:{artistName}"
    results = sp.search(q=query, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['id'] 
    else:
        print(f"Song '{songName}' not found.")
        return None

def getTrackVector(sp, songName, artistName):
    trackID = searchSong(sp, songName, artistName)
    if trackID:
        audio_features = sp.audio_features([trackID])[0]
        if audio_features:
            print(f"{songName} Audio Features: {audio_features}")
            return extractFeatures(audio_features)
    return None

song1 = "Blinding Lights" 
artist1 = "The Weeknd" 

song2 = "River Flows In You" 
artist2 = "Yiruma"

vector1 = getTrackVector(sp, song1, artist1)
vector2 = getTrackVector(sp, song2, artist2)

def findCosineSimilarity(vec1, vec2): 
  if vec1 is None or vec2 is None: 
     return "Vectors must be nonzero"
  ##initialize variables 
  dotProduct = 0 
  magnitudeV1 = 0 
  magnitudeV2 = 0 

  ##find common minimum length 
  minLength = min(len(vec1),len(vec2))

  for i in range(minLength): 
    dotProduct += vec1[i] * vec2[i] 
    magnitudeV1 += vec1[i] * vec1[i] 
    magnitudeV2 += vec2[i] * vec2[i] 
  
  if len(vec1) > len(vec2): 
    for i in range(minLength, len(vec1)): 
      magnitudeV1 += vec1[i] * vec1[i] 
  elif len(vec2) > len(vec1): 
    for i in range(minLength, len(vec2)): 
      magnitudeV2 += vec2[i] * vec2[i] 
  ##else if both vectors are equal length, original for loop suffices 
      
  ##calculate magnitudes: 
  magnitudeV1 = math.sqrt(magnitudeV1) 
  magnitudeV2 = math.sqrt(magnitudeV2) 

  if magnitudeV1 == 0 or magnitudeV2 == 0: 
    return 0 
  else: 
    cosineSimilarity = dotProduct / (magnitudeV1 * magnitudeV2)
    return cosineSimilarity

print(vector1) 
print(vector2) 


# print(findCosineSimilarity(vector1,vector2))
print(findCosineSimilarity(vector1, vector1))



def printSongDetails(sp, songName):
    results = sp.search(q=songName, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0] 
    else:
        print(f"Song '{songName}' not found.")
        return None

# songdetails1 = printSongDetails(sp, song1) 
# songdetails2 = printSongDetails(sp,song2)
# print(songdetails1)
# print(songdetails2)
    
