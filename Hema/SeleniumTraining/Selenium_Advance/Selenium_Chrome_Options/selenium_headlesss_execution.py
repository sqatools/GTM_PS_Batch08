from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chr_option
from selenium.webdriver.edge.options import Options as edge_option
from selenium.webdriver.firefox.options import Options as firefox_option

browser = 'chrome'

if browser.lower() == 'chrome':
    option1 = chr_option()
    option1.add_argument("--headless") # enable headless mode
    driver = webdriver.Chrome(options=option1)
    image_name = "chrome_image.png"
elif browser.lower() == 'edge':
    option2 = edge_option()
    option2.add_argument("--headless") # enable headless mode
    driver = webdriver.Edge(options=option2)
    image_name = "edge_image.png"
elif browser.lower() == 'firefox':
    option3 = firefox_option()
    option3.add_argument("--headless") # enable headless mode
    driver = webdriver.Firefox(options=option3)
    image_name = "firefox_image"


driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email").send_keys("user1@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("admin@123")
date = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
print(date)
driver.save_screenshot(f"{image_name}_{date}.png")
driver.find_element(By.NAME, "login").click()

driver.close()


