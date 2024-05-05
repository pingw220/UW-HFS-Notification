from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import smtplib
from email.message import EmailMessage
from twilio.rest import Client
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

login_page_url = 'https://myhfs.housing.uw.edu/myhfs'
driver.get(login_page_url)

username = driver.find_element(By.ID, 'weblogin_netid')
password = driver.find_element(By.ID, 'weblogin_password')

# Replace these with your actual username and password.
username.send_keys('username')
password.send_keys('password')

# Click the login button. Replace 'login_button_id' with the actual ID or name of the login button.
login_button = driver.find_element(By.ID, 'submit_button')
login_button.click()

wait = WebDriverWait(driver, 30)
trust_device_button = wait.until(EC.element_to_be_clickable((By.ID, "trust-browser-button")))
trust_device_button.click()

wait = WebDriverWait(driver, 15)

link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Select your room 2024-25!")))
link.click()

wait = WebDriverWait(driver, 10)
dropdown = Select(driver.find_element(By.ID, 'fld52336'))

# Select the building
dropdown.select_by_visible_text('Stevens Court')

search_button = driver.find_element(By.ID, 'btnSubmit')
search_button.click()

def check_room_availability(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "body"))
    )

    error_messages = driver.find_elements(By.CSS_SELECTOR, "p.Error")
    for message in error_messages:
        if "no rooms available" in message.text.lower():
            print("No rooms available.")
            return False

    print("Rooms available!")
    return True


gmail_user = 'your email'
gmail_password = 'password'

def send_notification_email():
    msg['Subject'] = "Room Availability Notification"
    msg['From'] = gmail_user
    msg['To'] = ""  # Recipient's email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()

while True:
    msg = EmailMessage()

    if check_room_availability(driver):
        msg.set_content("A room is now available!")
        send_notification_email()
        print("Notification sent: Room available!")
        break
    else:
        print("No rooms available. Checking again after some time...")

    driver.get('https://myhfs.housing.uw.edu/myhfs/SelectRoomResults.asp')
    time.sleep(30)
    link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Select your room 2024-25!")))
    link.click()

    wait = WebDriverWait(driver, 10)
    dropdown = Select(driver.find_element(By.ID, 'fld52336'))

    dropdown.select_by_visible_text('Stevens Court')

    search_button = driver.find_element(By.ID, 'btnSubmit')
    search_button.click()

input("Press Enter after you check the login succeeded, and the script will close the browser...")

driver.quit()