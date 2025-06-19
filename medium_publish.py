# medium_publish.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def publish_to_medium(title, content, tags):
    headers = {
        "Authorization": f"Bearer {os.getenv('MEDIUM_TOKEN')}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    me = requests.get("https://api.medium.com/v1/me", headers=headers).json()
    user_id = me['data']['id']

    data = {
        "title": title,
        "contentFormat": "markdown",
        "content": content,
        "tags": tags,
        "publishStatus": "public"
    }
    res = requests.post(f"https://api.medium.com/v1/users/{user_id}/posts", headers=headers, json=data)
    print("Status:", res.status_code, res.json())
