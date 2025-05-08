'''
common_url = "https://the-internet.herokuapp.com/

url = "https://the-internet.herokuapp.com/inputs"
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

def get_input_herkuapp():
    driver.get("https://the-internet.herokuapp.com/inputs")
    time.sleep(5)
    print("current url: ", driver.current_url)
    print("current title: ", driver.title)
    input_value = driver.find_element(By.XPATH, "//input[@type='number']")
    time.sleep(5)
    input_value.send_keys("2")
    time.sleep(10)

def get_text_a_b_test():
    driver.get("https://the-internet.herokuapp.com/abtest")
    print("current url: ", driver.current_url)
    print("title : ", driver.title)

    get_text = driver.find_element(By.XPATH, "//div[@id='content']//p")
    result = get_text.text
    time.sleep(5)
    print(result)

def get_add_remove_element():
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    print("current url: ", driver.current_url)
    print("title: ", driver.title)
    time.sleep(5)
    add_button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    print("Add button text: ", add_button.text)
    time.sleep(5)

    #to click add button for once we can use below option
    # add_button.click()
    # add_button.click()

    #to click add button for more than once we can use below opions
    for i in range(4):
        add_button.click()
    time.sleep(10)


    delete_buttons = driver.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")
    #print("Delete text: ", delete_button.text)
    for delete_button in delete_buttons:
        delete_button.click()
        time.sleep(5)

def get_float_elements():
    driver.get("https://the-internet.herokuapp.com/floating_menu")
    driver.implicitly_wait(5)
    float_items = driver.find_elements(By.XPATH, "//div[@id='menu']//a")

    for float_item in float_items:
        print(float_item.text)
        if float_item.text == 'Contact':
            float_item.click()
    time.sleep(5)
    print("url : ", driver.current_url)

def get_forgot_password():
    driver.get("https://the-internet.herokuapp.com/forgot_password")
    driver.implicitly_wait(5)
    print("title: ", driver.title)

    #doubt if invalid id is entered can we have validation here

    print("entering invalid email id")
    email_forgot_password = driver.find_element(By.ID, "email")
    email_forgot_password.send_keys("userabd1@hmail.com")

    retrive_password_button = driver.find_element(By.ID, "form_submit")
    retrive_password_button.click()

    time.sleep(5)

    print("last updated title: ", driver.title)
    print("current url: ", driver.current_url)

def flipkart_search():
    driver.get("https://www.flipkart.com/")
    time.sleep(5)

    search_text = driver.find_element(By.NAME, 'q')
    search_text.send_keys("table")
    time.sleep(5)
    search_text.click()

#get_input_herkuapp()
#get_text_a_b_test()
get_add_remove_element()
#get_float_elements()
#get_forgot_password()
#flipkart_search()
driver.close()
