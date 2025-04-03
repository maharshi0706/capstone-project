import json
import cv2
import numpy as np
import os
import glob
import re
from pathlib import Path
from moviepy.video.io.VideoFileClip import VideoFileClip # type: ignore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Capstone project root
DATASET_DIR = os.path.join(BASE_DIR, "Dataset\LABELS")  # Dataset folder
OUTPUT_DIR = os.path.join(BASE_DIR,"Dataset","Event_clips")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_clip(video_file, start_time, duration, output_file):
    try:
        with VideoFileClip(video_file) as video:
            start_time = min(max(0, start_time), video.duration - duration)
            end_time = min(start_time + duration, video.duration)

            clip = video.subclipped(start_time, end_time)
            clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=30)

        print(f"✅ Extracted: {output_file}")
    except Exception as e:
        print(f"❌ Error extracting {output_file}: {e}")

def loadJSON(BASE_DIR, labelName='Labels-v2.json'):
    # label_directory = Path(file_path)

    # for folder in label_directory.iterdir():
    #     if folder.is_dir():
    #         league_directory = folder
    #         for subfolders in league_directory.iterdir():
    #             if subfolders.is_dir():
    #                 year_directory = subfolders
    #                 for matches in year_directory.iterdir():
    #                     if matches.is_dir():
    #                         match_directory = matches
    #                         JSON_path = match_directory / labelName

    # if JSON_path.exists():
    for JSON_path in glob.glob(f"{DATASET_DIR}/**/Labels-v2.json", recursive=True):
        with open(JSON_path, 'r') as f:
            JSON_data = json.load(f)

        VideoURL:str = JSON_data['UrlLocal']
        annotations = JSON_data['annotations']
    
        # BASED ON VIDEO URL, find video and then trim based on annotations
        VIDEO_DIR = os.path.join(BASE_DIR, "Dataset","VIDEOS")
        
        match_video_path = os.path.join(VIDEO_DIR, VideoURL)
        match_video = Path(match_video_path)
        if match_video.exists():
            # Get each individual annotation
            for idx,annotation in enumerate(annotations):
                gameTime:str = annotation['gameTime']
                event_label = annotation['label'] # Event label such as goal, foul, etc
                team = annotation['team'] # The team that event belongs to:home or away
                position = annotation['position'] # ?

                event_label = re.sub(r'[<>:"/\\|?*]', '_', event_label)
                
                # Variable to determine which half of match to trim
                half = int(gameTime.split("-",1)[0].strip()) 
                
                # Convert MM:SS to seconds
                timestamp = gameTime.split("-",1)[1].strip()
                minutes,seconds = map(int, timestamp.split(':'))
                timestamp = (minutes * 60) + seconds

                video_file = os.path.join(match_video, "1_720p.mkv") if half == 1 else os.path.join(match_video,"2_720p.mkv")  
                # video = VideoFileClip(video_file)
                
                # Clip range (3 second before and after)
                start_time = max(0, timestamp - 3)
                duration = 6 # Total clip length (6 seconds)

                event_folder = os.path.join(OUTPUT_DIR, event_label)
                os.makedirs(event_folder, exist_ok=True)

                output_clip = os.path.join(event_folder, f"{event_label}_{idx}.mp4")

                if os.path.exists(output_clip):
                    print(f"⏭️ Skipping {output_clip} (Already exists)")
                    continue

                extract_clip(video_file, start_time, duration, output_clip)                
        else:
            print(f"Error: Match folder not found at {match_video}")
                            
loadJSON(BASE_DIR)