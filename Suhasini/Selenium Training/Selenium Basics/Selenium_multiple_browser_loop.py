import time
from selenium import webdriver

driver_list = [webdriver.Chrome(), webdriver.Firefox(), webdriver.Edge()]

for driver in driver_list:
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://www.facebook.com")

    # Set sleep time
    time.sleep(5)
    driver.close()
