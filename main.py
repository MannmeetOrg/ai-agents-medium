
from blog_utils import choose_topic, search_titles, rank_titles, generate_blog
from selenium_publish import publish_to_medium

query = choose_topic()
titles = search_titles(query)
top_titles = rank_titles(titles, query)
best_title = top_titles[0]
blog = generate_blog(best_title)
publish_to_medium(blog, best_title)
