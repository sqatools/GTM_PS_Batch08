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
    print("Current URL: ",driver.current_url)
    print("Website Title: ",driver.title)


def refresh_browser():
    driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
    driver.find_element(By.ID, "pass").send_keys("user@12345")
    time.sleep(5)
    driver.refresh()
    time.sleep(5)


def forward_and_back_operation():
    driver.find_element(By.LINK_TEXT, "Create new account").click()
    print("Current Title: ",driver.title)
    time.sleep(5)
    driver.back()
    print("Back Title: ",driver.title)

get_current_url_title()
time.sleep(5)