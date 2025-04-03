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
driver.maximize_window()
driver.get('https://automationbysqatools.blogspot.com/2021/05/dummy-website.html')
driver.implicitly_wait(10)

#dummy radi button
dummy_booking = driver.find_element(By.XPATH, '//div[@class="post-body entry-content"]//li[4]/input')
dummy_booking.click()

first_name = driver.find_element(By.XPATH, '//div[@class="post-body entry-content"]//div[2]/input[1]')
first_name.send_keys('abcuser1')

last_name = driver.find_element(By.XPATH, '//div[@class="post-body entry-content"]//div[2]/input[2]')
last_name.send_keys('sample')

gender_name = driver.find_element(By.XPATH, '//div[@class="post-body entry-content"]/div[2]/input[2]')
gender_name.click()

print("Travel details")

trip_detail = driver.find_element(By.XPATH, '//input[@id="oneway"]')
trip_detail.click()

from_city = driver.find_element(By.XPATH, '//input[@name="fromcity"]')
from_city.send_keys('chennai')

dest_city = driver.find_element(By.XPATH, '//input[@name="destcity"]')
dest_city.send_keys('bangalore')

receive_dummy_ticket = driver.find_element(By.XPATH, '//input[@id="whatsapp"]')
receive_dummy_ticket.click()

print("Billing_Details")

billing_name = driver.find_element(By.XPATH,'//input[@id="billing_name"]')
billing_name.send_keys('user1abc')

billing_phone =driver.find_element(By.XPATH, '//input[@id="billing_phone"]')
billing_phone.send_keys('1023456789')

billing_email = driver.find_element(By.XPATH, '//input[@id="billing_email"]')
billing_email.send_keys('abcuser1@gmail.com')

billing_address = driver.find_element(By.XPATH, '//input[@id="billing_address"]')
billing_address.send_keys('No3, abc street, chennai-48')

post_code = driver.find_element(By.XPATH, '//input[@name="postcode"]')
post_code.send_keys('600047')

predure = driver.find_element(By.XPATH, '//input[@id="Prefecture"]')
predure.send_keys('ert')

street_address = driver.find_element(By.XPATH, '//input[@id="street_address1"]')
street_address.send_keys('3, abc street')

street_address_2 = driver.find_element(By.XPATH, '//input[@id="street_address2"]')
street_address_2.send_keys('chennai - 48')

time.sleep(15)

driver.close()