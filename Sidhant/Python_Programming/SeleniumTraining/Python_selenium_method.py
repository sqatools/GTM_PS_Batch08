import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait( 10 )
driver.get( "https://www.facebook.com" )


def get_current_url_title():
    print( "current url:", driver.current_url )
    print( "Website title:", driver.title )


def refresh_browser():
    driver.find_element(By.ID,"email").send_keys("user@gmail.com")
    driver.find_element(By.ID,"pass").send_keys("user123")
    time.sleep( 5 )
    driver.refresh()
    time.sleep( 5 )


# get_current_url_title()
# time.sleep(5)
# refresh_browser()

def forward_and_back_operation():
    driver.find_element(By.LINK_TEXT,"Create new account").click()
    print(driver.title)
    time.sleep(5)
    driver.back()
    print(driver.title)
    time.sleep(5)
    driver.forward()
    print( driver.title )
    time.sleep(5)


#forward_and_back_operation()


def get_text_and_attribute_value():
    facebook_text = driver.find_element(By.TAG_NAME,"h2").text
    print("heading Text:",facebook_text)
    link_text = driver.find_element(By.LINK_TEXT,"Forgotten password?").get_attribute('href')
    print("forgot password",link_text)
    username_field = driver.find_element(By.ID,"email").get_attribute("placeholder")
    print(username_field)


#get_text_and_attribute_value()

def check_element_selected():
    driver.find_element(By.LINK_TEXT,"Create new account").click()
    radio_icon = driver.find_element(By.XPATH,"//input[@value='2']")
    print("before clicking",radio_icon.is_selected())
    time.sleep(5)
    radio_icon.click()
    print("After clicking",radio_icon.is_selected())
    time.sleep(5)

    print("element is enabled:",radio_icon.is_enabled())
    print( "element is displayed:", radio_icon.is_displayed() )
    time.sleep(5)


check_element_selected()
