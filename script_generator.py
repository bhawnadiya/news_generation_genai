import requests
import json
import time
from news_fetcher import fetch_news
from config import NEWS_LIMIT, BROADCAST_DURATION

def generate_news_script(user_topics):  # Added user_topics parameter
    """Generate news script based on user-selected topics"""
    # Gather articles
    articles = []
    for topic in user_topics:
        if topic_articles := fetch_news(topic):
            articles.extend(topic_articles)
    
    if not articles:
        return "Breaking News Update: No articles found on selected topics today."
    
    # Prepare prompt
    articles_text = "\n\n".join(
        f"{i+1}. [{art['source']}] {art['title']}: {art['content'][:200]}"
        for i, art in enumerate(articles)
    )
    
    duration_min = BROADCAST_DURATION // 60
    prompt = f"""
    You are a professional news anchor. Create a {duration_min}-minute broadcast script about: {', '.join(user_topics)}
    
    Structure:
    1. Brief introduction mentioning the topics
    2. 3-4 key news stories
    3. Smooth transitions between stories
    4. Neutral and professional tone
    5. Include a headline for each story
    6. Conclude with a sign-off
    
    Use these articles as sources:
    {articles_text}
    """

    # Generate script using LLaMA 2 via Ollama
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_ctx": 4096
                }
            }
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"Script generation failed: {e}")
        return "News update: Technical difficulties prevented script generation."