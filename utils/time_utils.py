def calculate_segments(script):
    # Simple segmentation logic (real implementation would use NLP)
    segments = []
    for part in script.split("\n\n"):
        if not part.strip():
            continue
        headline = part.split("\n")[0] if "\n" in part else "Headline"
        segments.append({
            "headline": headline,
            "text": part,
            "duration": min(60, 15 + len(part.split()) // 3)  # ~3 words/second
        })
    return segments
