
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://cislive.com/")
time.sleep(3)
driver.find_element(By.XPATH,"//div[@id ='navbarTogglerDemo01']//following::ul/li/a[text()='get in touch']").click()
time.sleep(8)