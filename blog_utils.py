# blog_utils.py
import random, os
import requests
from dotenv import load_dotenv
import google.generativeai as genai
import pkg_resources

print("Google GenAI SDK version:", pkg_resources.get_distribution("google-generativeai").version)

load_dotenv()

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-pro")

def choose_topic():
    return random.choice(["DevOps", "AI", "Microservices", "Cloud"])


def fetch_blog_ideas(topic):
    url = "https://serpapi.com/search"
    params = {
        "q": f"{topic} blog ideas",
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": 10,
        "engine": "google"
    }
    res = requests.get(url, params=params)
    return [r['title'] for r in res.json().get('organic_results', [])][:10]


def select_top_topics(ideas):
    prompt = f"Select the 5 most informative blog ideas from this list and explain why:\n{ideas}"
    try:
        response = model.generate_content(prompt)
        content = response.text
    except Exception as e:
        print(f"⚠️ Gemini API failed: {e}")
        return ideas[:5]
    lines = content.split("\n")
    return [line for line in lines if line.strip()][:5]


def generate_blog(topic):
    prompt = f"Write a blog post in simple English with technical terms on: {topic}"
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"⚠️ Gemini API failed: {e}")
        return f"Blog generation failed for topic: {topic}"
