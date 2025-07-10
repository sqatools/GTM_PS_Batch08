import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.find_element(By.LINK_TEXT,"What is Manual Testing").click()
driver.save_screenshot("main_window.png")
window_list = driver.window_handles
print(len(window_list))
time.sleep(5)
driver.switch_to.window(window_list[1])
driver.save_screenshot("new_window.png")

#verify header element

header_line = driver.find_element(By.XPATH,'//h3[@itemprop="name"]')
print("the line:",header_line)
assert header_line.text == "Manual Testing"
#switch to new tab
driver.find_element(By.LINK_TEXT,"API Testing").click()

# close new tab
driver.close()
time.sleep(5)
driver.switch_to.window(window_list[0])
driver.save_screenshot("homepage.png")
