import streamlit as st

def select_topics():
    predefined_topics = [
        "Technology", "Business", "Politics", "Science", "Entertainment"
    ]

    selected_categories = st.multiselect(
        "Select from predefined categories:",
        predefined_topics
    )

    custom_input = st.text_input(
        "Add custom topics (comma-separated, e.g., 'Telangana politics, AI breakthroughs')"
    )

    custom_topics = [topic.strip() for topic in custom_input.split(",") if topic.strip()]
    
    return selected_categories + custom_topics
