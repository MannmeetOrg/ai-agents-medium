import os
from dotenv import load_dotenv
from blog_utils import fetch_topic_ideas, select_top_topics, generate_blog
from selenium_publish import publish_to_medium

load_dotenv()

def main():
    topic = "Microservices"
    print("Chosen topic:", topic)

    ideas = fetch_topic_ideas(topic)
    print("Ideas fetched:", ideas)

    top5 = select_top_topics(ideas)
    print("Top 5 topics:", top5)

    best_topic = top5[0]
    title, content = generate_blog(best_topic)

    publish_to_medium(title, content)

if __name__ == "__main__":
    main()
