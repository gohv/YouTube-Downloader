from pytube import YouTube
from pytube import Playlist
import pytube.exceptions
import os

playlistUrl = input('Add the URL of the video with HTTPS and everything:\n')
try:
    playlist = Playlist(playlistUrl)
except KeyError:
    print('Not a Video Url \nExiting..')
else:
    user = os.path.expanduser('~') + '\Music\\' + playlist.title
    count = 0
    for video in playlist.videos:
        video.streams.get_by_itag(140).download(output_path = user)
        count += 1
        print(str(count) + "/" + str(len(playlist)) + " " + video.title)
        
print('Done...' + '\nOpening Folder...')
os.startfile(user)