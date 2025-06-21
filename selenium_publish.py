
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

def load_cookies(driver, cookies_path="cookies.json"):
    with open(cookies_path, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

def publish_to_medium(blog_content, title):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://medium.com/new-story")
    time.sleep(5)
    load_cookies(driver)
    driver.refresh()
    time.sleep(5)

    title_field = driver.find_element(By.TAG_NAME, "h1")
    title_field.click()
    title_field.send_keys(title)
    time.sleep(2)

    content_area = driver.find_element(By.CLASS_NAME, "section-inner")
    content_area.click()
    content_area.send_keys(blog_content[:2000])  # Avoid overflow in demo

    time.sleep(3)
    driver.quit()
