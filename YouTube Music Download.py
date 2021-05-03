from pytube import YouTube
import os

video = input('Add the URL of the video with HTTPS and everything:\n')
yt = YouTube(video)

print('The video you want is: \n'+ yt.title)
user = os.path.expanduser('~') + '\Music'
print('Downloading...')

# yt.streams.filter(only_audio=True)
stream = yt.streams.get_by_itag(140)
stream.download(output_path = user)
# print(yt.streams.filter(only_audio=True))
print('done...' + '\n opening...')
os.startfile(user)