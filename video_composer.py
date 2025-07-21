import os
import subprocess
from config import OUTPUT_DIR
from utils import get_video_duration

def compose_final_video(talking_head_path, subtitles_path, output_path):
    """Compose final video with proper sizing, positioning, and subtitles"""
    print("\n=== [compose_final_video] START ===")
    
    # Get video duration for accurate timing
    duration = get_video_duration(talking_head_path)
    
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Properly escape paths for FFmpeg
    safe_sub_path = subtitles_path.replace('\\', '/').replace(':', '\\:')
    
    # Build filtergraph for composition
    filter_complex = (
        f"color=black:s=1920x1080:d={duration}[bg];"  # Black background
        "[0:v]scale=500:500:force_original_aspect_ratio=increase,"
        "crop=500:500[head];"  # Properly scaled and cropped avatar
        f"[bg][head]overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2[main];"  # Centered positioning
        f"[main]subtitles='{safe_sub_path}':"  # Subtitles
        "force_style='FontName=Arial,FontSize=28,PrimaryColour=&HFFFFFF&,"
        "Outline=1,BorderStyle=1,Alignment=10,MarginV=50'[outv]"  # Subtitle styling
    )
    
    cmd = [
        "ffmpeg",
        '-i', talking_head_path,
        '-filter_complex', filter_complex,
        '-map', '[outv]',
        '-map', '0:a?',  # Use audio from input video
        '-c:v', 'libx264',
        '-preset', 'medium',
        '-crf', '18',
        '-r', '30',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-y', output_path
    ]
    
    print("Composing final video with FFmpeg command:")
    print(" ".join(cmd))
    
    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Final video composed at: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ Final composition failed: {e}")
        return None