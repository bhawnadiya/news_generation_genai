import subprocess

def convert_to_mp4(input_path, output_path):
    subprocess.call([
        'ffmpeg', '-i', input_path,
        '-c:v', 'libx264',
        '-crf', '23',
        '-preset', 'fast',
        '-c:a', 'aac',
        '-b:a', '192k',
        output_path
    ])