"""
1. Get Current URL
2. get current website title
3. refresh the browser
4. perform forward and back operation
5. get text of element
6. get attribute value
7. click operation
8. send_keys operation
9. check element is selected (radio, checkbox)
10. check element is displayed
11. check element is enabled
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com")

def get_current_url_title():
    print("current URL :", driver.current_url)
    print("website title :", driver.title)

def refresh_browser():
    driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("user@12345")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)


def forward_and_back_operation():
    driver.find_element(By.LINK_TEXT, "Create new account").click() # navigate to signup page
    print("current title:", driver.title)
    time.sleep(5)
    driver.back() # navigate to login page
    print("back title :", driver.title)
    time.sleep(5)
    driver.forward() # navigate to signup page
    print("forward title :", driver.title)
    time.sleep(5)

def get_text_and_attribute_value():
    facebook_text = driver.find_element(By.TAG_NAME, "h2").text
    print("Heading text :", facebook_text)
    link_element = driver.find_element(By.LINK_TEXT, "Forgotten password?")
    print("forgot password :", link_element.get_attribute("href"))

    username_field = driver.find_element(By.ID, "email")
    print(username_field)
    print("place holder value :", username_field.get_attribute("placeholder"))




def check_element_selected():
    driver.find_element(By.LINK_TEXT, "Create new account").click()
    male_radio = driver.find_element(By.XPATH, "//input[@value='2']")
    print("before clicking : ", male_radio.is_selected()) # False
    time.sleep(5)
    male_radio.click()
    print("After clicking : ", male_radio.is_selected()) # True
    print("element is enabled :", male_radio.is_enabled()) # True
    print("element is displayed :", male_radio.is_displayed())  # True
    time.sleep(5)


# get_current_url_title()
# time.sleep(5)
# refresh_browser()
# forward_and_back_operation()
# get_text_and_attribute_value()
check_element_selected()
driver.close()
