import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

topics_list = ['Software Testing Principles',
               'Grey Box Testing',
               'White Box Testing',
               'Functional Testing']
count = 1
for topic in topics_list:
    driver.find_element(By.LINK_TEXT, topic).click()

    # window_handles, will return the list of widow tabs are available with their ID
    windows_list = driver.window_handles
    #driver.current_window_handle
    print(windows_list)

    time.sleep(2)
    # switch to new tab
    driver.switch_to.window(windows_list[1])

    # take sacreenshot of new window
    driver.save_screenshot(f"new_window_{count}.png")

    # verify header on new window tab
    header_elem = driver.find_element(By.XPATH, "//h3[@itemprop='name']")
    header_elem.screenshot(f"header_{count}.png")
    print(header_elem.text)

    driver.close()

    # switch to main window
    driver.switch_to.window(windows_list[0])
    driver.save_screenshot("main_window.png")
    count += 1

time.sleep(2)
driver.close()










