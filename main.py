# main.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
from blog_utils import get_best_topic, generate_blog
from selenium_publish import publish_to_medium

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

load_dotenv()
def main():
    preferred_topics = ["DevOps", "AI/ML", "Cloud Platforms"]

    print("✅ Filtering blog ideas based on preferred topics...")
    best_topic = get_best_topic(preferred_topics)
    print("Chosen topic:", best_topic)

    title, content = generate_blog(best_topic)
    print("Generated title:", title)
    print("Generated content preview:\n", content[:500], "...")

    publish_to_medium(title, content)

if __name__ == "__main__":
    main()

