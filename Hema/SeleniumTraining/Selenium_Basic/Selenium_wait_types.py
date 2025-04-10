"""
# Types of waits in selenium

implicit wait : Whenever we want to apply a wait which is common for all the element, then we can use
               implicit wait
               ->  implicit wait is maximum timeout for an element to find in the DOM and it will move
                   ahead quickly even element is available in fraction of second.

explicit wait : explicit wait applies on specific element with specified condition, and this is also
                maximum timeout to find out the element within given period of time
fluent wait   : fluent wait is the polling frequency of the element to find out in DOM with the help of
                explicit wait.

static wait   :
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



def implicit_wait_check():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    t1 = time.time()
    try:
        driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Mumbai")
    except Exception as e:
        print(e)

    t2 = time.time()
    print("Total time taken:", t2-t1)


def check_explicit_wait_condition():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    wait = WebDriverWait(driver, timeout=15, poll_frequency=1)

    t1 = time.time()
    try:
        element = wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@id='fromcity1']")))
        element.send_keys("Bangalore")
    except Exception as e:
        print(e)

    t2 = time.time()
    print("total time take :", t2-t1)




#implicit_wait_check()
check_explicit_wait_condition()
