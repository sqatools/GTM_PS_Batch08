import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait( 10 )
driver.get( "https://automationbysqatools.blogspot.com/2020/08/alerts.html" )
alert = Alert( driver )


def handle_alert_box():
    driver.find_element( By.ID, "btnShowMsg" ).click()
    print( "given message:", alert.text )
    time.sleep( 4 )
    alert.accept()


# handle_alert_box()

def handle_confirm_box():
    driver.find_element( By.XPATH, "//button[@id='button']" ).click()
    time.sleep( 4 )
    print( "confirm msg:", alert.text )
    alert.accept()
    msg = driver.find_element( By.XPATH, "//p[@id='demo']" )
    assert msg.text == "You pressed OK!"
    print( msg.text )

    driver.find_element( By.XPATH, "//button[@id='button']" ).click()
    time.sleep( 4 )
    alert.dismiss()
    msg1 = driver.find_element( By.XPATH, "//p[@id='demo']" )
    assert msg1.text == "You pressed Cancel!"
    print( msg1.text )


#handle_confirm_box()


def handle_prompt_box():
    driver.find_element( By.XPATH, '//button[@id="promptbtn"]' ).click()
    time.sleep( 4 )
    input_val = "Sidhu"
    alert.send_keys( input_val )
    time.sleep( 4 )
    alert.accept()
    time.sleep( 4 )
    msg = driver.find_element( By.XPATH, '//p[@id="prompt"]' )
    assert msg.text == f"Hello {input_val}! How are you today?"
    print(msg.text)

handle_prompt_box()
