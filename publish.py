from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv(${{ secrets.MEDIUM_USER }})
password = os.getenv(${{ secrets.MEDIUM_PASS }})

def publish(title, content):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get("https://medium.com/m/signin")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in with email')]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in')]").click()
    time.sleep(5)

    driver.get("https://medium.com/new-story")
    time.sleep(5)

    title_field = driver.find_element(By.TAG_NAME, "textarea")
    title_field.send_keys(title)
    time.sleep(2)

    body = driver.find_element(By.XPATH, "//div[@role='textbox']")
    for line in content.split("\n"):
        body.send_keys(line)
        body.send_keys(Keys.ENTER)
    time.sleep(2)

    publish_button = driver.find_element(By.XPATH, "//span[text()='Publish']")
    publish_button.click()
    time.sleep(2)
    final_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Publish now')]")
    final_button.click()
    time.sleep(5)

    print("✅ Article published successfully!")
    driver.quit()

# Test
if __name__ == "__main__":
    title = "5 Emerging AI Tools for DevOps in 2025"
    content = """AI is transforming the DevOps landscape:
1. GitHub Copilot for CI/CD scripting
2. Harness AI for anomaly detection
3. ChatGPT plugins for Infrastructure as Code
4. K8s GPT tools for auto-diagnostics
5. AI observability platforms
"""
    publish(title, content)
