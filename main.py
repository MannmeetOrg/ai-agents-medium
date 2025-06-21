
from dotenv import load_dotenv
load_dotenv()

import os
from blog_utils import choose_topic, search_titles, rank_titles, generate_blog
from selenium_publish import publish_to_medium

query = choose_topic()
print(f"[Step 1] Chosen Topic: {query}")

titles = search_titles(query)
print(f"[Step 2] Titles found: {titles}")
if not titles:
    titles = [
        "Top 10 CI/CD Tools in DevOps",
        "Getting Started with LangChain",
        "AI Automation in Microservices",
        "Securing Serverless in AWS",
        "Monitoring with Prometheus and Grafana"
    ]

top_titles = rank_titles(titles, query)
print(f"[Step 3] Top Ranked Titles: {top_titles}")
if not top_titles:
    top_titles = titles[:5]

best_title = top_titles[0]
print(f"[Step 4] Best Title: {best_title}")

blog = generate_blog(best_title)
if not blog.strip():
    blog = f"### Offline Blog: {best_title}\n\nThis is a placeholder article on {best_title}. It will be updated once APIs are available."

print(f"[Step 5] Blog Generated: {blog[:300]}...")
publish_to_medium(blog, best_title)
