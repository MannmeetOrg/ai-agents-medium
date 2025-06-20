import os
import google.generativeai as genai
from dotenv import load_dotenv
from serpapi.google_search import GoogleSearch

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def get_model():
    try:
        return genai.GenerativeModel("gemini-1.5-flash")
    except:
        return genai.GenerativeModel("gemini-1.5-pro")

def fetch_blog_ideas(query):
    search = GoogleSearch({
        "q": f"{query} blog ideas",
        "api_key": os.getenv("SERPAPI_KEY")
    })
    results = search.get_dict()
    return [r["title"] for r in results.get("organic_results", []) if "title" in r]

def get_best_topic(preferred_topics):
    ideas = []
    for topic in preferred_topics:
        ideas += fetch_blog_ideas(topic)

    prompt = f"""You are a professional content strategist. Choose the 5 most interesting and educational blog post topics from the list below. Only return the selected titles:
{ideas}
"""
    model = get_model()
    response = model.generate_content(prompt)
    lines = response.text.strip().splitlines()
    filtered = [line.strip("- ").strip() for line in lines if line.strip()]
    return filtered[0] if filtered else "DevOps Trends in 2025"

def generate_blog(topic):
    prompt = f"""Write a 500-word SEO-friendly blog post titled '{topic}'. Structure it with an engaging introduction, 3 subheadings with details, and a conclusion. Make it professional yet readable."""
    model = get_model()
    response = model.generate_content(prompt)
    return topic, response.text
