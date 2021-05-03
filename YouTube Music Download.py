from pytube import YouTube
import pytube.exceptions
import os

video = input('Add the URL of the video with HTTPS and everything:\n')
try:
    yt = YouTube(video)
except pytube.exceptions.RegexMatchError:
    print('Not a Video Url \nExiting..')

else:
    print('The video you want is: \n'+ yt.title)
    savePath = os.path.expanduserPath('~') + '\Music'
    print('Downloading...')
    # yt.streams.filter(only_audio=True)
    stream = yt.streams.get_by_itag(140)
    stream.download(output_path = savePath)
    print('Done...' + '\nOpening Folder...')
    os.startfile(savePath)