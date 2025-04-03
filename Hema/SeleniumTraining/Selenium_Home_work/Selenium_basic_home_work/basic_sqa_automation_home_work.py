############################################
'''

Automating sqatools website

# https://automationbysqatools.blogspot.com/2021/05/dummy-website.html
'''
import time

###########################################

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://automationbysqatools.blogspot.com/2021/05/dummy-website.html')
driver.implicitly_wait(10)

first_name = driver.find_element(By.ID,'firstname')
first_name.send_keys('abcuser1')

gender_name = driver.find_element(By.ID, 'female')
gender_name.click()

print("Travel details")

trip_detail = driver.find_element(By.ID, 'oneway')
trip_detail.click()

from_city = driver.find_element(By.ID, 'fromcity')
from_city.send_keys('chennai')

dest_city = driver.find_element(By.ID, 'destcity')
dest_city.send_keys('bangalore')

receive_dummy_ticket = driver.find_element(By.ID, 'whatsapp')
receive_dummy_ticket.click()

print("Billing_Details")

billing_name = driver.find_element(By.ID, 'billing_name')
billing_name.send_keys('user1abc')

billing_phone =driver.find_element(By.ID, 'billing_phone')
billing_phone.send_keys('1023456789')

billing_email = driver.find_element(By.ID, 'billing_email')
billing_email.send_keys('abcuser1@gmail.com')

billing_address = driver.find_element(By.ID, 'billing_address')
billing_address.send_keys('No3, abc street, chennai-48')

post_code = driver.find_element(By.NAME, 'postcode')
post_code.send_keys('600047')

street_address = driver.find_element(By.ID, 'street_address1')
street_address.send_keys('3, abc street')

street_address_2 = driver.find_element(By.ID, 'street_address2')
street_address_2.send_keys('chennai - 48')

time.sleep(15)

driver.close()