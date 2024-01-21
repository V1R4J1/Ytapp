from pytube import YouTube, Channel
import re
import os


#Function for getting MP4 progressive video files
def mp4download(url):
    #Create youtube object
    yt = YouTube(url)

    #Filter file and stream types
    ytstream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
    
    #Error response
    if not ytstream:
        print("No Progressive MP4 streams for this video.")
        return None
    
    #Return downloaded file
    filepath = ytstream.download()

#MP3 file function
def mp3download(url):
    #Create youtube object
    yt = YouTube(url)

    #Filter file and stream types
    ytstream = yt.streams.filter(only_audio=True, file_extension='mp4').get_audio_only()

    if not ytstream:
        print("No MP3 streams for this video")
        return None
    
    #Download as MP4 file
    mp3stream = ytstream.download()
    mp3_file_name = mp3stream.split(".")[0] + ".mp3"

    #Convert to MP3 file
    os.rename(mp3stream, mp3_file_name)
    print(f"Download complete. Audio saved as: {mp3_file_name}")
    return mp3_file_name


#Display Video Info
def info(url):
    #Create Youtube object
    yt = YouTube(url)
    
    #Create channel object to extract channel name
    c = Channel(yt.channel_url)

    print(f"Video Title: {yt.title}")
    print(f"Views: {yt.views}")
    print(f"Upload Date: {yt.publish_date}")
    print(f"Channel Name: {c.channel_name}")

url = 0
p = True
while p == True:
    #User input (Call functions, input urls, etc)
    user_input = input("YtApp: ")

    #Checks if its a youtube url
    link_pattern = r"(?<=v=)[a-zA-Z0-9_-]{11}"
    x = re.search(link_pattern, user_input)
    if x:
        url = user_input
        continue
    
    #Checks for function calls
    formatted_input = str.lower(user_input)
    y = re.search("^download.*mp4$", formatted_input)
    z = re.search("^download.*mp3$", formatted_input)
    n = re.search("^display.*info$", formatted_input)

    if y:
        mp4download(url)
    elif z:
        mp3download(url)
    elif n:
        info(url)
    elif str.lower(user_input) == "end":
        p = False
    else:
        print("Please input a channel URL or refer to the readme file to check how to format your inputs")
