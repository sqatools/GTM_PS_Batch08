from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch a browser
driver = webdriver.Chrome()

# maximize browser window
driver.maximize_window()

#  set implicit wait for 20 sec.55
driver.implicitly_wait(20)

# open a facebook URL in the browser
driver.get("https://www.facebook.com")

# send username to field
driver.find_element(By.NAME, "email").send_keys("TestAdmin")

# send password to passwordfield
driver.find_element(By.NAME, "pass").send_keys("Admin@12345")

# click on login button
driver.find_element(By.NAME, "login").click()

# close current browser
driver.close()