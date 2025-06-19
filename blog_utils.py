# blog_utils.py
import random, os
import requests
import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    lines = res.choices[0].message.content.split("\n")
    return [line for line in lines if line.strip()][:5]


def generate_blog(topic):
    prompt = f"Write a simple-English blog post with technical terms on: {topic}"
    res = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content