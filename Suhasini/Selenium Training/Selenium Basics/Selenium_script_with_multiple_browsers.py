"""
# use below command to install selenium
-> pip install selenium
"""

import time
from selenium import webdriver

browser = 'edge'

if browser.lower() == 'chrome':
    driver = webdriver.Chrome()
elif browser.lower() == 'firefox':
    driver = webdriver.Firefox()
elif browser.lower() == 'edge':
    driver = webdriver.Edge()

# maximize browser window
driver.maximize_window()
# set implicit wait
driver.implicitly_wait(10)

# launch website URL on browser
driver.get("https://www.facebook.com")

# Set sleep time
time.sleep(5)
driver.close()


