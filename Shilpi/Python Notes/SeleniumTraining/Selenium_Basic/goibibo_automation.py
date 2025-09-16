from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/bus/")
time.sleep(3)
def book_bus(source,destination):
    source1=driver.find_element(By.XPATH,"//input[@name='autosuggestBusSRPSrcHomeName']")
    time.sleep(3)
    source1.send_keys(source)
    source_list=driver.find_elements(By.XPATH,"//div[@id='downshift-1-menu']//li")
    source_list[0].click()

    time.sleep(3)
    destination1=driver.find_element(By.XPATH,"//input[@placeholder='Enter Destination']")
    time.sleep(3)
    destination1.send_keys(destination)
    destination_list=driver.find_elements(By.XPATH,"//div[@id='downshift-2-menu']//li")
    destination_list[0].click()

    time.sleep(3)
    pick_a_date=driver.find_element(By.XPATH,"//input[@placeholder='Pick a date']")
    pick_a_date.click()
    date=driver.find_element(By.XPATH,"(//li[@style='color: black;']/span)[4]")
    date.click()
    search_button=driver.find_element(By.XPATH,"//button[text()='Search Bus']")
    search_button.click()
    update_search=driver.find_element(By.XPATH,"//span[text()='UPDATE SEARCH']")
    # wait=WebDriverWait(driver,timeout=10)
    # wait.until(ec.presence_of_element_located())

    assert update_search
    print("Assertion successful")
    time.sleep(10)
    driver.quit()

book_bus("Delhi","Allahabad")