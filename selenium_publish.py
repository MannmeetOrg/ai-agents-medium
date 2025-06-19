# selenium_publish.py
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()


def publish_to_medium(title, content):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get("https://medium.com/m/signin")
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in with email')]").click()
        time.sleep(3)

        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys(os.getenv("MEDIUM_USERNAME"))
        email_input.send_keys(Keys.RETURN)
        time.sleep(3)

        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(os.getenv("MEDIUM_PASSWORD"))
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get("https://medium.com/new-story")
        time.sleep(5)

        title_box = driver.find_element(By.TAG_NAME, "h1")
        title_box.click()
        title_box.send_keys(title)

        para_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        para_box.click()
        for line in content.split("\n"):
            para_box.send_keys(line)
            para_box.send_keys(Keys.ENTER)
            time.sleep(0.1)

        publish_btn = driver.find_element(By.XPATH, "//button[.='Publish']")
        publish_btn.click()
        time.sleep(2)

        final_publish_btn = driver.find_element(By.XPATH, "//button[.='Publish now']")
        final_publish_btn.click()

        print("✅ Blog published successfully.")

    except Exception as e:
        print("❌ Error publishing to Medium:", str(e))
    finally:
        driver.quit()