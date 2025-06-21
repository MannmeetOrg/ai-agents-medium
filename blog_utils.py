
import os
import random
from serpapi import GoogleSearch
import openai
import requests

DOMAINS = ["DevOps", "AI", "Microservices", "Cloud Platform"]
TOPIC_KEYWORDS = {
    "DevOps": ["CI/CD", "GitOps", "Terraform", "Monitoring", "SRE"],
    "AI": ["GenAI", "LLMs", "LangChain", "Vector DB", "Prompt Engineering"],
    "Microservices": ["Service Mesh", "API Gateway", "gRPC", "Resilience", "Dapr"],
    "Cloud Platform": ["AWS", "GCP", "Azure", "Serverless", "IAM", "Networking"]
}

def choose_topic():
    domain = random.choice(DOMAINS)
    topic = random.choice(TOPIC_KEYWORDS[domain])
    return f"{domain} - {topic}"

def search_titles(query):
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": 10
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [r["title"] for r in results.get("organic_results", [])]

def rank_titles(titles, query):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Rank these titles for clarity and informativeness on the topic '{query}':\n" + "\n".join(titles)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4
        )
        return response.choices[0].message["content"].split("\n")[:5]
    except:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        headers = {"Content-Type": "application/json"}
        data = {"contents":[{"parts":[{"text": prompt}]}]}
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}",
            headers=headers,
            json=data
        )
        candidates = response.json().get("candidates", [])
        return candidates[0]["content"]["parts"][0]["text"].split("\n")[:5] if candidates else titles[:5]

def generate_blog(title):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Write a blog on the topic: '{title}' using simple English with technical details. Length: ~700 words."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return response.choices[0].message["content"]
    except:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        headers = {"Content-Type": "application/json"}
        data = {"contents":[{"parts":[{"text": prompt}]}]}
        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}",
            headers=headers,
            json=data
        )
        candidates = response.json().get("candidates", [])
        return candidates[0]["content"]["parts"][0]["text"] if candidates else ""
