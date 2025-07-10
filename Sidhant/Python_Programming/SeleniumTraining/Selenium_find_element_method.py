import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait( 10 )
driver.get( "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html" )
checkbox_list = driver.find_elements( By.XPATH, "//div[@align='left']//ul//input[@type='radio']" )


def checkbox_data():
    for checkbox in checkbox_list:
        print( "before:", checkbox.is_selected() )
        checkbox.click()
        print( "after click", checkbox.is_selected() )
        time.sleep( 3 )


# checkbox_data()

import time


from selenium import webdriver
from selenium.webdriver.common.by import By


def implicit_wait_check():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    t1 =time.time()
    try:
        driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("Mumbai")
        time.sleep(3)
    except Exception as e:
        print(e)
        pass
    t2 =time.time()
    print("total time taken:",t2-t1)

# implicit_wait_check()


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def check_explicit_wait_condition():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    wait = WebDriverWait(driver,timeout=10)
    t1 = time.time()
    try:
        element = wait.until(ec.element_to_be_clickable((By.XPATH,"//input[@id='fromcity']"))).send_keys("Bangalore")
        time.sleep(4)
    except Exception as e:
        print(e)
    t2 =time.time()
    print("total time taken:",t2-t1)

check_explicit_wait_condition()