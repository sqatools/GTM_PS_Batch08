import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://facebook.com")

time.sleep(5)
driver.close()

