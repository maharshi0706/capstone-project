import os
from dotenv import load_dotenv
from SoccerNet.Downloader import SoccerNetDownloader

SOCCERNET_PASS = os.environ.get("soccernet_password")
print(f"PASSWORD:{SOCCERNET_PASS}")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
DATASET_DIR = os.path.join(BASE_DIR, "Dataset", "VIDEOS")  

os.makedirs(DATASET_DIR, exist_ok=True)

mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory=DATASET_DIR)
mySoccerNetDownloader.password = 's0cc3rn3t'  

# video_files = ["1_720p.mkv", "2_720p.mkv"]  

# games_to_download = ["game_1", "game_2"]  

# print("\nDownloading match videos for testing...")
# mySoccerNetDownloader.downloadGames(games=games_to_download, files=video_files, split=["test"])

# Optionally, you can download annotations if you need them for testing
# json_files = ["Labels-v2.json"]  # Annotation file
# mySoccerNetDownloader.downloadGames(files=json_files, split=["test"])

# test_games = [
#     "england_epl_2014-2015_1-1_arsenal-crystalpalace",
#     "england_epl_2014-2015_1-2_burnley-chelsea"
# ]
# video_files = ["1_720p.mkv", "2_720p.mkv"]  # First and second half

print("\nDownloading selected match videos for testing...")
mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv"], split=["test"])
# for game in test_games:
#     print(f"Downloading: {game}")
#     mySoccerNetDownloader.downloadGame(game, files=video_files)

print("\nDownload complete! Files are saved in:", DATASET_DIR)
