import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

from spiders import ApplyLeavePageSpider

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

    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'oxd-select-text-input')))
    
    time.sleep(3)
    
    
    # Selecting the leave type
    leave_type_dropdown = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-select-text-input')))
    leave_type_dropdown.click()  
    leave_type_option = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@role="option"]//span[text()="CAN - FMLA"]')))
    leave_type_option.click()  
    time.sleep(3)
    
    # selecting the from date of the leave
    from_date_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/input')))
    from_date_field.clear()
    from_date_field.send_keys('2024-19-07')
    time.sleep(3)
    
    # Selecting the date to which the leave has to be taken
    to_date_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/input')))
    driver.execute_script("arguments[0].value = '2024-22-07';", to_date_field)
    time.sleep(3)
    
    # Commenting for the reason of leave 
    comments_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/textarea')))
    comments_field.send_keys('Wanted to attend the Cricket nationals camp. ')
    time.sleep(3)
    
    apply_leave_page_spider = ApplyLeavePageSpider()
    apply_leave_page_spider.parse(driver.page_source)
    
    # Click the apply button
    apply_button = driver.find_element(By.CLASS_NAME, 'orangehrm-left-space')
    apply_button.click()
    
    time.sleep(5)
    
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList')
    
    time.sleep(10)
    print("im here")
    

finally:
    driver.quit()
