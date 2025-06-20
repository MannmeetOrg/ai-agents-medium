import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def publish_to_medium(title, content):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        wait = WebDriverWait(driver, 15)

        # Step 1: Load Medium and set domain
        driver.get("https://medium.com")
        time.sleep(3)

        # Step 2: Load cookies
        with open("cookies.json", "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            if "sameSite" in cookie and cookie["sameSite"] not in ["Lax", "Strict", "None"]:
                del cookie["sameSite"]
            for field in ["storeId", "hostOnly", "session", "id"]:
                cookie.pop(field, None)
            driver.add_cookie(cookie)

        # Step 3: Open new story
        driver.get("https://medium.com/new-story")
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1")))
        time.sleep(2)

        # Step 4: Fill title
        title_box = driver.find_element(By.XPATH, "//h1")
        driver.execute_script("arguments[0].scrollIntoView(true);", title_box)
        title_box.click()
        title_box.send_keys(title)
        time.sleep(2)

        # Step 5: Fill body
        body_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='textbox']")))
        driver.execute_script("arguments[0].scrollIntoView(true);", body_box)
        body_box.click()
        body_box.send_keys(content)
        time.sleep(5)

        # Step 6: Publish
        publish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Publish']]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", publish_button)
        publish_button.click()
        time.sleep(2)

        confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Publish now']]")))
        confirm_button.click()
        time.sleep(5)

        print("✅ Blog successfully published to Medium!")

    except Exception as e:
        print("❌ Error publishing to Medium:", str(e))

    finally:
        driver.quit()
