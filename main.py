import streamlit as st
st.set_page_config(page_title="Bhawna News Generator", layout="centered")

import os
from datetime import datetime
from topic_selector import select_topics
from script_generator import generate_news_script
from narration import generate_tts_narration
from avatar_animator import create_talking_head, create_static_avatar_video
from subtitle_generator import generate_subtitles
from video_composer import compose_final_video
from config import OUTPUT_DIR


def run_app():
    st.title("🎙️ Bhawna's AI News Broadcast Generator")

    st.markdown("This app generates a full AI-powered news broadcast from selected topics.")

    st.subheader("Step 1: Choose Topics")
    user_topics = select_topics()

    if st.button("Start News Broadcast"):
        if not user_topics:
            st.warning("Please select at least one topic or add a custom one.")
            return

        with st.spinner("Creating folders..."):
            os.makedirs(f"{OUTPUT_DIR}/scripts", exist_ok=True)
            os.makedirs(f"{OUTPUT_DIR}/audio", exist_ok=True)
            os.makedirs(f"{OUTPUT_DIR}/videos", exist_ok=True)

        start_time = datetime.now()

        st.success(f"✅ Selected topics: {', '.join(user_topics)}")

        # Step 2: Generate Script
        st.subheader("Step 2: Generating Script...")
        script = generate_news_script(user_topics)
        st.text_area("📝 Generated Script", script, height=300)

        script_path = f"{OUTPUT_DIR}/scripts/script_{datetime.now().strftime('%H%M%S')}.txt"
        with open(script_path, "w") as f:
            f.write(script)

        # Step 3: Generate Narration
        st.subheader("Step 3: Generating Narration...")
        narration_path = os.path.join(OUTPUT_DIR, "audio", "narration.mp3")
        generate_tts_narration(script, narration_path)
        st.audio(narration_path)

        # Step 4: Create Avatar Video
        # st.subheader("Step 4: Creating Avatar Video")
        # try:
        #     talking_head_path = create_talking_head(narration_path)
        #     if not talking_head_path or not os.path.exists(talking_head_path):
        #         raise Exception("Talking head failed")
        # except:
        # st.warning("⚠️ Talking head animation failed. Using static avatar instead.")
        talking_head_path = create_static_avatar_video(narration_path)

        # Step 5: Generate Subtitles
        st.subheader("Step 4: Generating Subtitles")
        subtitles_path = generate_subtitles(script, narration_path)
        st.success("Subtitles generated!")

        # Step 6: Compose Final Video
        st.subheader("Step 5: Composing Final Video")
        output_path = os.path.join(OUTPUT_DIR, "videos", f"broadcast_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")
        compose_final_video(talking_head_path, subtitles_path, output_path)

        st.video(output_path)
        st.success("✅ News broadcast generated successfully!")
        st.markdown(f"📥 [Download Final Video]({output_path})")

        st.write(f"⏱ Total time: {datetime.now() - start_time}")


if __name__ == "__main__":
    run_app()
