
from config import OUTPUT_DIR
from gtts import gTTS
import os

def generate_tts_narration(text, output_path):
    """Generate TTS narration and save to specified path"""
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        tts = gTTS(text=text, lang="en", slow=False)
        tts.save(output_path)
        print(f"Audio narration saved to: {output_path}")
        return output_path
    except Exception as e:
        print(f"❌ Error generating narration: {e}")
        return None