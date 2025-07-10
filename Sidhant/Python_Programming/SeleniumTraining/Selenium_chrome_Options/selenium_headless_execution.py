from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chr_option
option1 = chr_option()
option1.add_argument("--headless")  # enable headless mode
driver = webdriver.Chrome(options=option1)#Headless mode runs Chrome without a UI (invisible),
# which is useful for automation, CI/CD, or servers without GUIs.


driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("admin@123")
date = datetime.now().strftime("%d_%m_%y_%H_%M_%S") #datetime format
driver.save_screenshot("login1_page.png")
driver.find_element(By.NAME,"login").click()
driver.close()