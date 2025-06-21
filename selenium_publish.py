
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

def load_cookies(driver, cookies_path="cookies.json"):
    with open(cookies_path, "r") as f:
        cookies = json.load(f)
    for cookie in cookies:
        if "sameSite" in cookie and cookie["sameSite"] not in ["Strict", "Lax", "None"]:
            cookie.pop("sameSite")
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"[Cookie Warning] {e}")

def publish_to_medium(blog_content, title):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://medium.com/new-story")
    time.sleep(5)
    load_cookies(driver)
    driver.refresh()
    time.sleep(5)

    try:
        title_field = driver.find_element(By.TAG_NAME, "h1")
        title_field.click()
        title_field.send_keys(title)
        time.sleep(2)

        content_area = driver.find_element(By.CLASS_NAME, "section-inner")
        content_area.click()
        content_area.send_keys(blog_content[:2000])
        time.sleep(3)
    except Exception as e:
        print("[Publishing Error]", e)
    finally:
        driver.quit()
