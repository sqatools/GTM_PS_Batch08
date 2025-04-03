"""
1.Get current URL
2.Get current website title
3.Refresh the browser
4.Perform forward and back operation
5.Get text of element
6.Get attribute value
7.click operation
8.send_keys operation
9.Check element is selected(radio, check box)
10.check element is displayed
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.chrome
driver.maximize_window()
driver.implicity_wait(10)
driver.get("http://www.faacebook.com")


def get_current_url_tittle():
    print("current URL :", driver.current_url)
    print("website title :", driver.title)

def refresh_browser():
    driver.find_elements(By.ID, "email").send_keys("user1@gmail.com")
    driver.find_elements(By.ID, "pass").send_keys("user@12345")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)



def forward_and_back_operation():
    driver.find_element(By.LINK_TEXT, "Create new account").click()
    print("current title:", driver.title)
    time.sleep(5)
    driver.back()
    print("back title :", driver.title)
    time.sleep(5)
    driver.forward()
    print("forward title :", driver.title)
    time.sleep(5)

def get_text_and_attribute_value():
    facebook_text = driver.find_element(By.TAG_NAME, "h2").text
    print("Heading text :", facebook_text)
    link_element = driver.find_element(By.LINK_TEXT, "Forgotten password?")
    print("forgot password :", link_element.get_attribute("href"))

    username_field = driver.find_element(By.ID, "email")
    print("place holder value :", username_field.get.attribute("placeholder"))

