import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")

upload_element = driver.find_element(By.ID, "myFile")
upload_element.send_keys(["E:\\Filesdata\\count_name.txt"])

time.sleep(5)

driver.find_element(By.XPATH, "(//input[@type='submit'])[1]").click()

time.sleep(5)
driver.close()

# Home work
# https://www.goibibo.com/

