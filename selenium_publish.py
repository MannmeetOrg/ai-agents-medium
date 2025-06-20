from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json

def publish_to_medium(title, content):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get("https://medium.com")
    time.sleep(5)

    # Load cookies from cookies.json
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.get("https://medium.com/new-story")
    time.sleep(5)

    try:
        title_elem = driver.find_element(By.XPATH, '//h1')
        title_elem.click()
        title_elem.send_keys(title)

        time.sleep(2)
        body_elem = driver.find_element(By.XPATH, '//div[@role="textbox"]')
        body_elem.click()
        body_elem.send_keys(content)

        time.sleep(2)

        print("✅ Blog drafted on Medium")
    except Exception as e:
        print("❌ Error publishing to Medium:", e)

    driver.quit()
