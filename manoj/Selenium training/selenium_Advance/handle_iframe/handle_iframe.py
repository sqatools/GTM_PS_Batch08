import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

iframe_element = driver.find_element(By.XPATH, "//iframe[@name='globalsqa']")
driver.switch_to.frame(iframe_element)


mobile_menu = driver.find_elements(By.ID, "mobile_menu_toggler")
mobile_menu.click()

time.sleep(5)