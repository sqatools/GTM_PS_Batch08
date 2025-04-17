import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# find_element method return the list of web elements.

def select_all_checkboxes():
    checkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkbox_list:
        print("Before click :", checkbox.is_selected())
        checkbox.click()
        print("After click :", checkbox.is_selected())
        time.sleep(2)
        print("_"*50)


def select_all_radios_buttons():
    radios_btn_list = driver.find_elements(By.XPATH, "//div[@align='left']/ul//input[@type='radio']")
    for radio in radios_btn_list:
        print("Before click :", radio.is_selected())
        radio.click()
        print("After click :", radio.is_selected())
        time.sleep(2)
        print("_"*50)




#select_all_checkboxes()
select_all_radios_buttons()
driver.close()

# //div[@align='left']/ul//input[@type='radio']
