import requests
from config import NEWS_API_KEY, NEWS_LIMIT

def fetch_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}&sortBy=publishedAt&pageSize={NEWS_LIMIT}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        
        if not articles:
            return None
        
        return [{
            "title": art["title"],
            "source": art["source"]["name"],
            "url": art["url"],
            "content": art.get("content") or art.get("description") or ""
        } for art in articles if art.get("title")]
    
    except Exception as e:
        print(f"News fetch error: {e}")
        return None