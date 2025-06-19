# main.py
from blog_utils import choose_topic, fetch_blog_ideas, select_top_topics, generate_blog
from selenium_publish import publish_to_medium

def main():
    topic = choose_topic()
    print(f"Chosen topic: {topic}")

    ideas = fetch_blog_ideas(topic)
    print("Ideas fetched:", ideas)

    top5 = select_top_topics(ideas)
    print("Top 5 topics:", top5)

    best_topic = top5[0]  # Use the first suggestion
    blog_content = generate_blog(best_topic)

    publish_to_medium(best_topic, blog_content)

if __name__ == "__main__":
    main()