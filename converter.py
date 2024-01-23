from pytube import YouTube, Channel
import re
import os

LINK_PATTERN = r"(?<=v=)[a-zA-Z0-9_-]{11}"

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

def display_commands():
    # Displays all possible commands and their use cases 
    print('\n--------------------HELP--------------------\n')
    print('Download mp3/mp4 file for a YT vid: download <filetype> <url>')
    print('Display info about YT vid: display info <url>')
    print('help: Provide info about commands, you just did it!')
    print('end: Quits the app')
    print('\n--------------------HELP--------------------\n')

# Boilerplate
if __name__ == '__main__':
    # Runs a loop, app ends when broken away from this function
    while True:
        # Get User input
        user_input = input('YtApp: ')
        # Separate input command into individual words, stored as a list
        command_word_arr = user_input.split()

        # Validate appropriate command length
        if len(command_word_arr) > 3 or len(command_word_arr) < 1:
            print("Invalid command length, use the command 'help' for assistance")
            continue

        # Check for help and quit commands
        elif len(command_word_arr) == 1:
            if user_input == 'help':
                display_commands() # Displays all possible commands and their uses
            elif user_input == 'end':
                break # Quits app
            else:
                print("Invalid one word command, use the command 'help' for assistance")
                continue
        elif re.search(LINK_PATTERN, command_word_arr[-1]): # Checks whether a YT url has been entered
            url = command_word_arr[-1]
            if command_word_arr[0] == 'download': # Download a new yt vid
                if command_word_arr[1].lower() == 'mp3':
                    mp3download(url) # Audio
                elif command_word_arr[1].lower() == 'mp4':
                    mp4download(url) # Video
                else:
                    print("Invalid filetype, use the command 'help' for assistance")
                    continue
            elif command_word_arr[0] == 'display' and command_word_arr[1] == 'info':
                info(url) # Display YT vid info
            else:
                print("Invalid yt vid command, use the command 'help' for assistance")
                continue
        else:
            print("Invalid command, use the command 'help' for assistance")
            continue