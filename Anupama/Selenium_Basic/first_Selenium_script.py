"""
# use below command to install selenium
-> pip install selenium
"""
import time

from selenium import webdriver
# Initiate a webdriver
driver = webdriver.Chrome()
# maximize browser window
driver.maximize_window()
# set implicit wait
driver.implicitly_wait(10)

# launch website URL on browser.
driver.get("https://www.facebook.com")

# Set sleep time
time.sleep(5)
driver.close()

