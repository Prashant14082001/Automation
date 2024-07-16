import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

driver = webdriver.Chrome()

try:
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    wait = WebDriverWait(driver, 20)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    password_field = driver.find_element(By.NAME, 'password')
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    
    # Wait for the dashboard to load completely
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'oxd-topbar-header-breadcrumb-module')))
    
    time.sleep(5)
    
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave')

    # Wait for the leave application page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'oxd-select-text-input')))
    
    

    
    time.sleep(5)

finally:
    driver.quit()
