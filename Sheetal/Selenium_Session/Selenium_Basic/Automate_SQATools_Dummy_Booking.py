##Libraries used ##
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import  NoSuchElementException,TimeoutException



# https://automationbysqatools.blogspot.com/2021/05/dummy-website.html

## Constants
Website_Link = 'https://sqatools.in/dummy-booking-website/'


##  Initialize Webdriver  ###
def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def check_booking_website(driver):
    driver.get(Website_Link)
    try:
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//h1[text()='Dummy Booking Website']")
    except NoSuchElementException as e:
        print(f"The element is not located: {e}")

def book_ticket(driver):
    driver.find_element(By.XPATH,"//span[text()='    First Name    ']/following-sibling::input[@id='firstname']").send_keys("Sheetal")
    driver.find_element(By.XPATH,"//span[text()='    Last Name     ']/following-sibling::input[@id='firstname']").send_keys("S")
    driver.find_element(By.XPATH,"// input[ @ id = 'birthday']").send_keys('04/11/1995')
    driver.find_element(By.XPATH,"//span[text()='Sex*']/following-sibling::input[@id='female']").click()

    time.sleep(3)



def main():
    driver = initialize_driver()
    try:
        check_booking_website(driver)
        book_ticket(driver)
    except TimeoutException:
        print("Time Out")



if __name__ == "__main__" :
    main()