from pytube import YouTube
from sys import argv



input = str(input("Enter the link of the video you want to download: "))


link = input

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length of video: ", yt.length, "seconds")


print("Downloading.....")

yd = yt.streams.get_highest_resolution()
yd.download('VideoDownloads') 


print("Download completed!!")