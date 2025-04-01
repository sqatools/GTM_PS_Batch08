import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Locators in Selenium:

1. ID = "id"
2. XPATH = "xpath"
3. LINK_TEXT = "link text"
4. PARTIAL_LINK_TEXT = "partial link text"
5. NAME = "name"
6. TAG_NAME = "tag name"
7. CLASS_NAME = "class name"
8. CSS_SELECTOR = "css selector"

"""

# Initiate a webdriver
driver = webdriver.Chrome()
# maximize browser window
driver.maximize_window()
# set implicit wait
driver.implicitly_wait(10)

# launch website URL on browser.
driver.get("https://www.facebook.com")

"""
# identify element ID Locator
driver.find_element(By.ID, "email").send_keys("user1@gmail.com")
time.sleep(2)

# identify element with NAME Locator
pass_elem = driver.find_element(By.NAME, "pass")
pass_elem.clear()
pass_elem.send_keys("user@12345")

time.sleep(2)

driver.find_element(By.NAME, "login").click()
time.sleep(2)
"""

# identify element with LINK_TEXT and PARTIAL_LINK_TEXT
#driver.find_element(By.LINK_TEXT, "Create new account").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Create new").click()

# Set sleep time
time.sleep(10)
driver.close()


# Home work website:
# https://automationbysqatools.blogspot.com/2021/05/dummy-website.html

