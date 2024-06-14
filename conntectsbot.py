from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import random

# Path to the ChromeDriver executable
driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/login")

# Wait for the username field to be present and enter the username
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='session_key']"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='session_password']"))
)

username.send_keys("barkatalimchandioad@gmail.com")
password.send_keys("Barkat")

time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()
time.sleep(2)

n_pages = 3

for n in range(1, n_pages + 1):
    driver.get(f"https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page="+str(n))
    time.sleep(2)

    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(6, 7):
        try:
            # Click on "Message" button
            driver.execute_script("arguments[0].click();", message_buttons[i])
            time.sleep(2)

            # Activate main div
            main_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[starts-with(@class, 'msg-form__msg-content-container')]"))
            )
            driver.execute_script("arguments[0].click();", main_div)

            # Type message
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            all_span = driver.find_elements(By.TAG_NAME, "span")
            all_span = [s for s in all_span if s.get_attribute("aria-hidden") == "true"]

            idx = [*range(3, 23, 2)]
            greetings = ["Hello", "Hi", "Hey", "Ahoy", "Yo yo", "Sup"]
            all_names = []

            for j in idx:
                name = all_span[j].text.split(" ")[0]
                all_names.append(name)

            greetings_idx = random.randint(0, len(greetings) - 1)
            message = f"{greetings[greetings_idx]} {all_names[i]}, Sorry, I didn't mean to bother you, I'm just building a Linkedin Web Scraper Bot and testing its' capabilities... My apologies!:) This is not Barkat , this message is automated"

            paragraphs[-5].send_keys(message)
            time.sleep(2)

            # Send message
            submit = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit.click()
            time.sleep(2)

            # Close div
            close_button = driver.find_element(By.XPATH, "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
            driver.execute_script("arguments[0].click();", close_button)
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
