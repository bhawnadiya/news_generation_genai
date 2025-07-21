AI News Broadcast Generator - Comprehensive Documentation

🚀 Project Overview
The AI News Broadcast Generator automates the creation of personalized video news broadcasts. It integrates multiple AI components to:
Select trending/custom topics
Generate scripts using real-time news data
Convert text to lifelike narration (TTS)
Animate an avatar with synchronized lip movements (SadTalker)
Add subtitles and compose the final video
Output: Professional broadcast videos stored in outputs/ directory.

🔄 Workflow Diagram


📂 File Structure & Descriptions
File/Folder
Key Functionality
main.py
Orchestrates pipeline execution (topic→script→audio→avatar→video)
topic_selector.py
CLI for selecting news categories/custom topics (e.g., "Technology", "Climate Change")
script_generator.py
Generates human-like scripts using GPT models + real-time news data
news_fetcher.py
Fetches live articles via NewsAPI/Pexels APIs
narration.py
Converts scripts to audio using TTS (gTTS/Coqui)
avatar_animator.py
Animates avatar (SadTalker) driven by audio input
subtitle_generator.py
Creates .srt subtitles synced to narration timings
video_composer.py
Merges avatar video, audio, and subtitles into final MP4
image_generator.py
Optional: Fetches/generates background visuals
check.py
Validates/installs dependencies (SadTalker, PyTorch, etc.)
config.py
Stores API keys, paths, and constants
utils.py
Helper functions (file I/O, timing, logging)
requirements.txt
Python dependencies
SadTalker/
Submodule for facial animation (models + inference scripts)
assets/
Static resources (avatar images, fonts, templates)
outputs/
Generated content (scripts/audio/videos/subtitles)


⚙️ Installation Process
1. Clone Repository & Initialize
bash
git clone https://github.com/yourusername/news-broadcast-generator.git
cd news-broadcast-generator
git submodule update --init  # Initialize SadTalker
2. Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install Dependencies
bash
pip install -r requirements.txt
# Alternative: Auto-install via check.py
python check.py
4. Download SadTalker Models
bash
bash SadTalker/scripts/download_models.sh
Manual Setup: Place model checkpoints in:
SadTalker/checkpoints/
gfpgan/weights/
5. Configure API Keys
Create .env file:
ini
NEWS_API_KEY="your_newsapi_key"
PEXELS_API_KEY="optional_pexels_key"
TTS_ENGINE="gtts"  # Options: gtts, coqui

▶️ Usage
Run Pipeline:
bash
python main.py
Interactive Steps:
Select news categories (e.g., 1 for Technology)
Enter custom topics (e.g., "Quantum Computing")
Wait 2-5 mins for processing
Output:
Final video → outputs/final_broadcast.mp4
Example Output Features:
🎙️ AI-narrated script about latest AI breakthroughs
👩 Avatar with natural lip-syncing
📝 Burned-in subtitles
🎼 Background visuals (if enabled)

🔧 Troubleshooting
SadTalker Errors: Verify model paths in SadTalker/scripts/download_models.sh
Missing Dependencies: Run python check.py --force-reinstall
API Limits: Use .env to switch TTS engines if gTTS fails

 Credits
SadTalker for avatar animation
NewsAPI for live news data
Python Libraries: moviepy, gfpgan, gTTS, transformers

📄 License
MIT License - See LICENSE

Ready to create your first broadcast? Run python main.py! 🎥




Results:






