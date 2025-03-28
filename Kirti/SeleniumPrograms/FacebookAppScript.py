import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.facebook.com")

# click on Create new Account
driver.find_element(By.LINK_TEXT, "Create new account").click()

# Enter the user details
driver.find_element(By.NAME,"firstname").send_keys("Advik")
driver.find_element(By.NAME,"lastname").send_keys("Gadakh")

day = Select(driver.find_element(By.ID,"day"))
day.select_by_value("21")
month = Select(driver.find_element(By.ID,"month"))
month.select_by_value("4")
year = Select(driver.find_element(By.ID,"year"))
year.select_by_value("2022")




time.sleep(5)
driver.close()