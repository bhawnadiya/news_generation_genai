import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# API configuration
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
WAV2LIP_API_KEY = os.getenv("WAVV2LIP_API_KEY", "")
FFMPEG_PATH = r"D:\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"
# Path configuration
ASSETS_DIR = "assets"
OUTPUT_DIR = "outputs"
AVATAR_PATH = os.path.join(ASSETS_DIR, "avatar.png")
FONT_PATH = os.path.join(ASSETS_DIR, "font.ttf")
FALLBACK_IMAGE = os.path.join(ASSETS_DIR, "fallback.jpg")
SADTALKER_PATH = os.path.join(os.getcwd(), "SadTalker")
SADTALKER_INFERENCE_PATH = os.path.join(SADTALKER_PATH, "inference.py")  # News settings (removed fixed topics)
OUTPUT_RESOLUTION = (1280, 720)
NEWS_LIMIT = 3  # Number of articles per topic
BROADCAST_DURATION = 170  # Seconds (2m50s)