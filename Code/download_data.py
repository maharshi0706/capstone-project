import os
from dotenv import load_dotenv
from SoccerNet.Downloader import SoccerNetDownloader

SOCCERNET_PASS = os.environ.get("soccernet_password")
print(f"PASSWORD:{SOCCERNET_PASS}")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Capstone project root
DATASET_DIR = os.path.join(BASE_DIR, "Dataset\VIDEOS")  # Dataset folder

# Ensure dataset directory exists
os.makedirs(DATASET_DIR, exist_ok=True)

# Initialize SoccerNet Downloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory=DATASET_DIR)
mySoccerNetDownloader.password = 's0cc3rn3t'  # Replace with actual password
video_files = ["1_720p.mkv", "2_720p.mkv"]  # First and second half match videos
json_files = ["Labels-v2.json"]  # Annotation file

# Download videos
print("\nDownloading match videos...")
mySoccerNetDownloader.downloadGames(files=video_files, split=["train"])

# Download JSON annotations
# print("\nDownloading annotation files...")
# mySoccerNetDownloader.downloadGames(files=json_files, split=["train"])

print("\nDownload complete! Files are saved in:", DATASET_DIR)
