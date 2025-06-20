import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def publish_to_medium(title, content):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Step 1: Load Medium home to set domain context
        driver.get("https://medium.com")
        time.sleep(3)

        # Step 2: Load cookies from JSON
        with open("cookies.json", "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            # Clean invalid or unnecessary fields
            if "sameSite" in cookie and cookie["sameSite"] not in ["Lax", "Strict", "None"]:
                del cookie["sameSite"]
            for field in ["storeId", "hostOnly", "session", "id"]:
                cookie.pop(field, None)

            driver.add_cookie(cookie)

        # Step 3: Go to new story page
        driver.get("https://medium.com/new-story")
        time.sleep(5)

        # Step 4: Enter title and content
        title_box = driver.find_element(By.XPATH, "//h1")
        title_box.click()
        title_box.send_keys(title)

        time.sleep(2)

        body_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        body_box.click()
        body_box.send_keys(content)

        time.sleep(5)

        # Step 5: Click on Publish
        publish_button = driver.find_element(By.XPATH, "//button[.//span[text()='Publish']]")
        publish_button.click()
        time.sleep(3)

        confirm_button = driver.find_element(By.XPATH, "//button[.//span[text()='Publish now']]")
        confirm_button.click()
        time.sleep(5)

        print("✅ Blog successfully published to Medium!")

    except Exception as e:
        print("❌ Error publishing to Medium:", str(e))

    finally:
        driver.quit()
