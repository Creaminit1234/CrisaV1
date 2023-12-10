from pytube import YouTube, Playlist
import pytube # dont mind this import
import colorama
import os


os.system("cls")

colorama.init(autoreset=False)
RED = colorama.Fore.RED
RED_BACK = colorama.Back.RED
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
WHITE = colorama.Fore.WHITE
COLOR_RESET = colorama.Fore.RESET
COLOR_RESET_BACK = colorama.Back.RESET
LOGO = f"""{GREEN}                                                      
                                                                                 
  ,ad8888ba,               88                            8b           d8     88  
 d8"'    `"8b              ""                            `8b         d8'   ,d88  
d8'                                                       `8b       d8'  888888  
88             8b,dPPYba,  88  ,adPPYba,  ,adPPYYba,       `8b     d8'       88  
88             88P'   "Y8  88  I8[    ""  ""     `Y8        `8b   d8'        88  
Y8,            88          88   `"Y8ba,   ,adPPPPP88         `8b d8'         88  
 Y8a.    .a8P  88          88  aa    ]8I  88,    ,88          `888'          88  
  `"Y8888Y"'   88          88  `"YbbdP"'  `"8bbdP"Y8           `8'           88  
                                                                                 
"""
def set_cmd_size(width, height):
    os.system(f"mode con: cols={width} lines={height}")

set_cmd_size(85, 20)

print(f"{LOGO} {COLOR_RESET}")

print(f"""
{BLUE}
Enter [1] to download a video
Enter [2] to download a entire playlist
""")
deci = int(input(f"Enter your option (1 or 2): {GREEN}"))

if deci == int("1"):
    videolink = str(input(f"{BLUE}YouTube video's link: {GREEN}"))
    try:
        yt = YouTube(videolink)


        video_stream = yt.streams.get_highest_resolution()
        download_directory = 'downloads'

        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        print(f"{BLUE}Downloading...{COLOR_RESET}")
        video_stream.download(download_directory)
        print(f"{GREEN}Download complete!{COLOR_RESET}")

    except Exception as e:
        print(f"{RED}An error occurred: {e} {COLOR_RESET}")

elif deci == int("2"):
    playlist_link = input(f"{BLUE}YouTube Playlist Link:{GREEN} ")

    try:
        playlist = Playlist(playlist_link)

        # Iterating through each video in the playlist
        for video in playlist.videos:
            # Getting the highest resolution stream
            video_stream = video.streams.get_highest_resolution()

            # Setting the download path
            download_path = './playlist_downloads'  # Replace with your preferred directory

            # Downloading the video
            print(f"{BLUE}Downloading the video '{video.title}'...{COLOR_RESET}")
            video_stream.download(download_path)
            print(f"{GREEN}Video '{video.title}' downloaded!{COLOR_RESET}")

        print(f"{GREEN}Entire playlist has been downloaded!{COLOR_RESET}")

    except Exception as e:
        print(f"{RED}An error occurred: {e}{COLOR_RESET}")
 



