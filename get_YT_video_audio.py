#Getting Video from Youtube
from pytube import YouTube
url="https://www.youtube.com/watch?v=Q1EeHessyaE&ab_channel=CampusX"
download_path=None
YouTube(url).streams.first().download(download_path,filename="yt_video")

# Extracting the audio from video file
import moviepy.editor as mp
audio=mp.VideoFileClip(r"yt_video")
audio.audio.write_audiofile(r"yt_audio.mp3")
