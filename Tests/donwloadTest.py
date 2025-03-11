from pytubefix import YouTube
import os
from pytubefix.exceptions import VideoUnavailable
# url input from user


try:
 yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
 if yt.check_availability() == False:
   print("error")
except VideoUnavailable:
 print(f'Video is unavaialable, skipping.')
except:
 print("Error occured when reading video url")
else: 
 print(yt.title)
 # extract only audio
 video = yt.streams.filter(only_audio=True).first()
 # check for destination to save file
 
 
 print("Enter the destination (leave blank for current directory)")
 destination = str(input(">> ")) or '.'
 
 # download the file
 out_file = video.download(output_path=destination)
 
 # save the file
 base, ext = os.path.splitext(out_file)
 new_file = base + '.mp3'
 os.rename(out_file, new_file)
 
 # result of success
 print(yt.title + " has been successfully downloaded.")
 
 