from pytube import YouTube
from pytube import Playlist
import os

playlistUrl = input('Add the URL of the video with HTTPS and everything:\n')
playlist = Playlist(playlistUrl)
user = os.path.expanduser('~') + '\Music\\' + playlist.title

count = 0
for video in playlist.videos:
    video.streams.get_by_itag(140).download(output_path = user)
    count += 1
    print(str(count) + " " + video.title)
