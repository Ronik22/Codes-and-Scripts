import requests
import re
import youtube_dl

"""
CONSTANTS
"""
CHANNEL_NAME = "pantechsolutions"
DOWNLOAD_PATH = "E:/Projects/YT Download Recent/YTDownloads/"


channel = f"https://www.youtube.com/user/{CHANNEL_NAME}"
html = requests.get(channel + "/videos").text
url = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()

f = open("history.txt", "r")

if url in f.readline(): 
    pass
else:
    # download video from YT
    ydl_opts = {
        'outtmpl': f'{DOWNLOAD_PATH}%(title)s.%(ext)s'
    }
    zxt = url.strip()
    def dwl_vid():
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([zxt])

    dwl_vid()  

    # append to the top of a history file
    with open("history.txt",'r') as contents:
        save = contents.read()
    with open("history.txt",'w') as contents:
        contents.write(url + "\n")
    with open("history.txt",'a') as contents:
        contents.write(save)
