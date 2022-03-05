#Playlist download yuotube

from pytube import Playlist

py= Playlist("https://www.youtube.com/playlist?list=PLAXqhIH8yzwdfgVqYNPTb40ofxvFXe2XA")

print(f'Downloading: {py.title}')

for video in py.videos:
    video.streams.first().download()
      
      
