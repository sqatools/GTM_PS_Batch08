"""
# use below command to install selenium
-> pip install selenium
"""
import time

from selenium import webdriver

driver_list = [webdriver.Chrome(),  webdriver.Firefox(), webdriver.Edge()]

for driver in driver_list:
    # maximize browser window
    driver.maximize_window()
    # set implicit wait
    driver.implicitly_wait(10)

    # launch website URL on browser.
    driver.get("https://www.facebook.com")

    # Set sleep time
    time.sleep(5)
    driver.close()
