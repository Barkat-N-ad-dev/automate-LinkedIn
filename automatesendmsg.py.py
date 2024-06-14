from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import random

# Path to the ChromeDriver executable
driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=service)
driver.get("https://linkedin.com")

# Wait for the username and password fields to be present
username = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='session_key']"))
)
password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='session_password']"))
)

# Enter the username and password
username.send_keys("barkatalimchandioad@gmail.com")
password.send_keys("Barkat")

# Wait for the submit button to be clickable and click it
submit = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
submit.click()

# Allow some time for the page to load
time.sleep(5)

# Number of pages to navigate through
n_pages = 3

for n in range(1, n_pages + 1):
    driver.get(f"https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page={n}")
    time.sleep(2)

    all_buttons = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
    )
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(len(message_buttons)):
        try:
            # Click on "Message" button
            driver.execute_script("arguments[0].click();", message_buttons[i])
            time.sleep(2)

            # Activate main div
            main_div = WebDriverWait(driver, 20).until(
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
            message = f"{greetings[greetings_idx]} {all_names[i]}, Hello"
            paragraphs[-5].send_keys(message)
            time.sleep(2)

            # Send message
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            time.sleep(2)

            # Close div
            close_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]"))
            )
            driver.execute_script("arguments[0].click();", close_button)
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
import random

# Path to the ChromeDriver executable
driver_path = r"C:\webdriver\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=service)
driver.get("https://linkedin.com")

# Wait for the username and password fields to be present
username = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='session_key']"))
)
password = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='session_password']"))
)

# Enter the username and password
username.send_keys("barkatalimchandioad@gmail.com")
password.send_keys("Barkat")

# Wait for the submit button to be clickable and click it
submit = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
submit.click()

# Allow some time for the page to load
time.sleep(5)

# Number of pages to navigate through
n_pages = 3

for n in range(1, n_pages + 1):
    driver.get(f"https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page={n}")
    time.sleep(2)

    all_buttons = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
    )
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    for i in range(len(message_buttons)):
        try:
            # Click on "Message" button
            driver.execute_script("arguments[0].click();", message_buttons[i])
            time.sleep(2)

            # Activate main div
            main_div = WebDriverWait(driver, 20).until(
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
            message = f"{greetings[greetings_idx]} {all_names[i]}, How are you sir hope you are doing well! Thanks,"

            paragraphs[-5].send_keys(message)
            time.sleep(2)

            # Send message
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            time.sleep(2)

            # Close div
            close_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]"))
            )
            driver.execute_script("arguments[0].click();", close_button)
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
