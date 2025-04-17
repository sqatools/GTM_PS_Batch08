import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chr_option
from selenium.webdriver.edge.options import Options as edge_option
from selenium.webdriver.firefox.options import Options as firefox_option

option1 = chr_option()
prefs_dict = {"download.default_directory": "E:\\Filesdata\\DownloadFiles",
         "download.prompt_for_download": False,
         "download.directory_upgrade": True,
         "safebrowsing_for_trusted_sources_enabled": False,
         "safebrowsing.enabled": False}
#option1.add_argument("--headless") # enable headless mode
option1.add_argument("--disable-notifications")
option1.add_argument("--window-size=1920*1080")
#option1.add_argument("--incognito")
option1.add_experimental_option("prefs", prefs_dict)
option1.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=option1)
image_name = "chrome_image.png"

driver.maximize_window()
driver.implicitly_wait(15)
"""
driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("admin@123")
date = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
print(date)
driver.save_screenshot(f"{image_name}_{date}.png")
driver.find_element(By.NAME, "login").click()
"""

driver.get("https://www.python.org/downloads/")

down_btn = driver.find_element(By.XPATH, "(//a[text()='Download Python 3.13.3'])[2]")
down_btn.click()

time.sleep(10)

#driver.close()


