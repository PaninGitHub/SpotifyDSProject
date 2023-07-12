#Imports
print("Starting program")
      
import pandas as pd
import os 
import methods as met


#Settings
csv_name = "spotify_data.csv"
abs_path = os.path.dirname(__file__)
csv_path = os.path.join(abs_path, csv_name)
method_path = os.path.join(abs_path, "Methods")
audio_features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature']



#Imports CSV and drops missing variables
df = pd.read_csv(csv_path)
df.dropna(inplace = True)

met.graph2(df, False, audio_features)












