##############################################################
'''
Facebook home work with xpath locator
'''
##############################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = "chrome"

if browser == 'chrome':
    driver = webdriver.Chrome()
elif browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == 'edge':
    driver = webdriver.Edge()
else:
    print("invalid browser")

driver.get("https://facebook.com")

driver.maximize_window()

driver.implicitly_wait(10)

#create account
create_account = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
create_account.click()

time.sleep(5)

#Firstname
first_name = driver.find_element(By.XPATH, '//input[@aria-label="First name"]')
first_name.send_keys('abcuser1')

#lastname
last_name = driver.find_element(By.XPATH, '//input[@aria-label="Surname"]')
last_name.send_keys('sample')

#gender_radio_button
gender_radio_button = driver.find_element(By.XPATH, '//input[@value="1"]')
gender_radio_button.click()

#mobile_number
mobile_num = driver.find_element(By.XPATH, '//input[@aria-label="Mobile number or email address"]')
mobile_num.send_keys('0123456789')

#password
password = driver.find_element(By.XPATH, '//input[@aria-label="New password"]')
password.send_keys('User1_abc123')

#signup
sign_up_button = driver.find_element(By.XPATH, '//div[@id="reg_form_box"]/div[11]/button')
sign_up_button.click()

time.sleep(10)
driver.close()