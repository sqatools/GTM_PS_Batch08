"""
# use below command to install selenium
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.facebook.com')
driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("user1")
# driver.find_element(By.NAME,"login").click()

driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.implicitly_wait(10)


url = "https://www.facebook.com/r.php?entry_point=login"
current_url = driver.current_url
if current_url == url:
    driver.find_element(By.NAME,"firstname").send_keys("Sheetal")
    driver.find_element(By.NAME,"lastname").send_keys("S")
    driver.find_element(By.ID,"day").send_keys(27)
    driver.find_element(By.ID, "month").send_keys("Mar")
    driver.find_element(By.ID,"year").send_keys(2024)
    driver.find_element(By.XPATH,"//input[@type='radio' and @value= '1']").click()
    driver.find_element(By.NAME,"reg_email__").send_keys(9999977665)
    driver.find_element(By.ID,"password_step_input").send_keys("user2")
    time.sleep(5)
driver.close()
