from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "liborhavranek91@gmail.com"
ACCOUNT_PASSWORD = "9684pepe"

chrome_driver_path = Service(r"C:\Development\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(2)
driver.maximize_window()
time.sleep(1)
accept = driver.find_element(by=By.XPATH, value='//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')

sign_button = driver.find_element(by=By.LINK_TEXT, value='Přihlásit se')
accept.click()
time.sleep(2)
sign_button.click()
time.sleep(5)

email_form = driver.find_element(by=By.ID, value="username")
email_form.send_keys(ACCOUNT_EMAIL)
time.sleep(1)
password_form = driver.find_element(by=By.ID, value='password')
password_form.send_keys(ACCOUNT_PASSWORD)
time.sleep(1)
password_form.send_keys(Keys.ENTER)
time.sleep(5)

