import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def load_cookies(driver, path):
    with open(path, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            if 'sameSite' in cookie and cookie['sameSite'] == 'None':
                cookie['sameSite'] = 'Strict'
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            try:
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Skipping cookie due to error: {e}")

def publish_to_medium(title, content):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Load Medium with cookies
        driver.get("https://medium.com/")
        driver.delete_all_cookies()
        load_cookies(driver, "cookies.json")

        # Navigate to new story page
        driver.get("https://medium.com/new-story")
        time.sleep(5)

        # Fill title
        title_box = driver.find_element(By.TAG_NAME, "h1")
        title_box.click()
        title_box.send_keys(title)

        # Fill content
        para_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        para_box.click()
        for line in content.split("\n"):
            para_box.send_keys(line)
            para_box.send_keys(Keys.ENTER)
            time.sleep(0.1)

        # Click Publish buttons
        publish_btn = driver.find_element(By.XPATH, "//button[.='Publish']")
        publish_btn.click()
        time.sleep(2)

        final_publish_btn = driver.find_element(By.XPATH, "//button[.='Publish now']")
        final_publish_btn.click()
        print("✅ Blog published successfully.")

    except Exception as e:
        print("❌ Error publishing to Medium:", e)
    finally:
        driver.quit()
