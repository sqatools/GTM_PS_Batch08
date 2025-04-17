import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

driver.find_element(By.LINK_TEXT, "What is Manual Testing").click()
driver.save_screenshot("main_window.png")

# window_handles, will return the list of widow tabs are available with their ID
windows_list = driver.window_handles
#driver.current_window_handle
print(windows_list)

time.sleep(2)
# switch to new tab
driver.switch_to.window(windows_list[1])

# take sacreenshot of new window
driver.save_screenshot("new_window.png")

# verify header on new window tab
header_elem = driver.find_element(By.XPATH, "//h3[@itemprop='name']")
print(header_elem.text)
assert header_elem.text == 'Manual Testing'

# click on API testing
driver.find_element(By.LINK_TEXT, "API Testing").click()

# close newly open tab
driver.close()
time.sleep(2)

# switch to main window
driver.switch_to.window(windows_list[0])
driver.save_screenshot("main_window2.png")

time.sleep(2)
driver.close()










