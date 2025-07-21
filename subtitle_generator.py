import os
import json
import math
from moviepy.editor import AudioFileClip
from config import OUTPUT_DIR, FONT_PATH

def generate_subtitles(script, audio_path):
    # Split script into phrases
    phrases = [p.strip() for p in script.split('.') if p.strip()]
    
    # Calculate timing based on audio
    audio = AudioFileClip(audio_path)
    total_duration = audio.duration
    phrase_duration = total_duration / len(phrases)
    
    # Generate SRT subtitle file
    srt_path = os.path.join(OUTPUT_DIR, "subtitles.srt")
    with open(srt_path, "w") as f:
        for i, phrase in enumerate(phrases):
            start = i * phrase_duration
            end = (i + 1) * phrase_duration
            
            # Convert to SRT time format
            start_time = f"{math.floor(start/3600):02}:{math.floor(start%3600/60):02}:{start%60:06.3f}".replace('.', ',')
            end_time = f"{math.floor(end/3600):02}:{math.floor(end%3600/60):02}:{end%60:06.3f}".replace('.', ',')
            
            f.write(f"{i+1}\n")
            f.write(f"{start_time} --> {end_time}\n")
            f.write(f"{phrase}\n\n")
    
    return srt_path