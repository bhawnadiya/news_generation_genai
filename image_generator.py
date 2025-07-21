import requests
import os
from config import PEXELS_API_KEY, OUTPUT_DIR
from datetime import datetime

def download_image(query):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"query": query, "per_page": 1, "orientation": "landscape"}
    
    try:
        # Search for image
        search_url = "https://api.pexels.com/v1/search"
        search_res = requests.get(search_url, headers=headers, params=params)
        search_res.raise_for_status()
        
        if not search_res.json().get("photos"):
            return None
        
        # Download image
        photo = search_res.json()["photos"][0]
        img_url = photo["src"]["original"]
        img_data = requests.get(img_url, stream=True)
        img_data.raise_for_status()
        
        # Save image
        os.makedirs(f"{OUTPUT_DIR}/images", exist_ok=True)
        img_path = f"{OUTPUT_DIR}/images/{query[:20]}_{datetime.now().strftime('%H%M%S')}.jpg"
        
        with open(img_path, "wb") as f:
            for chunk in img_data.iter_content(1024):
                f.write(chunk)
                
        return img_path
    except Exception as e:
        print(f"Image download failed: {e}")
        return None