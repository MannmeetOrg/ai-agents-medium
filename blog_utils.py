import os
import requests
import google.generativeai as genai

SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

def fetch_topic_ideas(topic):
    url = "https://serpapi.com/search.json"
    params = {
        "q": topic + " blog ideas",
        "hl": "en",
        "gl": "us",
        "api_key": SERPAPI_KEY,
    }
    response = requests.get(url, params=params)
    results = response.json()
    ideas = [item['title'] for item in results.get("organic_results", [])[:10]]
    return ideas

def select_top_topics(ideas):
    prompt = """Select the 5 most useful and interesting blog topics from the list below:

{}""".format("\n".join(f"- {i}" for i in ideas))
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
    except Exception:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
    lines = [line.strip("- ") for line in response.text.split("\n") if line.strip()]
    return lines[:5]

def generate_blog(topic):
    prompt = f"Write a detailed blog post on the topic: '{topic}' in simple, clear language for beginners. Include examples and use technical terms only when helpful."
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
        response = model.generate_content(prompt)
    except Exception:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
    return topic, response.text.strip()
