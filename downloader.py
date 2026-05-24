import yt_dlp
import os

# Create download folder automatically:
# C:\Users\<yourname>\Downloads\YouTube
download_folder = os.path.join(
    os.path.expanduser("~"),
    "Downloads",
    "YouTube"
)

os.makedirs(download_folder, exist_ok=True)

url = input("Enter YouTube URL: ")

print("\nSelect download type:")
print("1. Video")
print("2. MP3 Audio")

choice = input("Enter choice (1/2): ")

if choice == "1":

    print("\nChoose quality:")
    print("1. 360p")
    print("2. 720p")
    print("3. 1080p")
    print("4. Best")

    q = input("Enter quality: ")

    quality_map = {
        "1": "bestvideo[height<=360]+bestaudio/best[height<=360]",
        "2": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "3": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "4": "best"
    }

    ydl_opts = {
        'format': quality_map.get(q, 'best'),
        'outtmpl': os.path.join(
            download_folder,
            '%(title)s.%(ext)s'
        ),
        'merge_output_format': 'mp4'
    }

elif choice == "2":

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(
            download_folder,
            '%(title)s.%(ext)s'
        ),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

else:
    print("Invalid choice")
    exit()

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("\nDownload complete")
    print("\nSaved at:")
    print(download_folder)

except Exception as e:
    print("\nError:", e)