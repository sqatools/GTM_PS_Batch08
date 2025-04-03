##########################################
'''
Automating facebook create account page via selenium

'''
import time

#########################################

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
#for cross browsers
driver_lists = [webdriver.Chrome(), webdriver.Firefox(), webdriver.Edge()]

for driver in driver_lists:
    driver.maximize_window()
    
    #implementation continues
    pass
'''

browser = 'chrome'

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()
elif browser.lower() == 'edge':
    driver = webdriver.Edge()
else:
    print("please check browser namr")

#maximizing the window

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://facebook.com")
time.sleep(5)

#create account
create_account = driver.find_element(By.LINK_TEXT, 'Create new account')
create_account.click()

time.sleep(5)

#Firstname
first_name = driver.find_element(By.NAME, 'firstname')
first_name.send_keys('abcuser1')

#lastname
last_name = driver.find_element(By.NAME, 'lastname')
last_name.send_keys('sample')

#radio_button [DOUBT]
gender_radio_button = driver.find_element(By.ID,'sex')
gender_radio_button.click()

#mobile_number
mobile_num = driver.find_element(By.NAME, 'reg_email__')
mobile_num.send_keys('0123456789')

#password
password = driver.find_element(By.ID, 'password_step_input')
password.send_keys('User1_abc123')

#signup
sign_up_button = driver.find_element(By.NAME,'websubmit')
sign_up_button.click()

time.sleep(10)
driver.close()