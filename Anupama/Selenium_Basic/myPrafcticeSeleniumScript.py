import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.facebook.com')
time.sleep(5)
login = browser.find_elements(By.XPATH,'')
browser.close()

