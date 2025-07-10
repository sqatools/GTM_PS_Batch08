import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
iframe_element = driver.find_element(By.XPATH,"//iframe[@name='globalSqa']")
time.sleep(2)
driver.switch_to.frame(iframe_element)   # Use driver.switch_to.frame() to interact with elements inside an iframe.
mobile_menu = driver.find_element(By.ID,"mobile_menu_toggler")
mobile_menu.click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(13)
menu_tab = driver.find_element(By.XPATH,"//div[@id='menu']//a[@href='https://www.globalsqa.com/testers-hub/']")
menu_tab.click()
time.sleep(5)