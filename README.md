Spotify Cosine Similarity
This Python script calculates the cosine similarity between the audio feature vectors of two songs using the Spotify API. It allows users to compare songs based on specific attributes such as danceability, energy, acousticness, and more.

Features
  - Fetches audio features of songs using the Spotify Web API.
  - Calculates cosine similarity to determine the similarity between two songs.
  - Prints detailed audio feature data for the given songs.

Requirements
  - Python 3.7 or higher
  - The spotipy library

Configuration
Before running the script, set up a Spotify Developer account and create an application. Update the following credentials in the script:
client_id
client_secret
redirect_uri
These credentials are used to authenticate with the Spotify API.
