'''

Facebook

'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

def create_new_fb_account():
    create_account = driver.find_element(By.XPATH, "//a[@data-testid='open-registration-form-button']")
    create_account.click()

    time.sleep(2)

    print("title of webpage is: ", driver.title)

    assert driver.title == "Sign up for Facebook"

def facebook_text_box_in_create_account():
    first_name = driver.find_element(By.XPATH, "//input[@aria-label='First name']")
    first_name.send_keys("abcd")

    sur_name = driver.find_element(By.XPATH, "//input[@aria-label='Surname']")
    sur_name.send_keys("efg")

    mobile_number = driver.find_element(By.NAME, "reg_email__")
    mobile_number.send_keys("8001080010")

    password = driver.find_element(By.NAME, "reg_passwd__")
    password.send_keys("A1b2c3!801")

    time.sleep(2)

def select_drodown(ele,value):
    pass
def facebook_dropdown_in_create_account():
    date_option = driver.find_element(By.ID, "day")
    select_obj = Select(date_option)
    select_obj.select_by_value("30")
    time.sleep(2)

    month_option = driver.find_element(By.ID, "month")
    select_obj = Select(month_option)
    select_obj.select_by_visible_text("Nov")

    year_option = driver.find_element(By.ID, "year")
    select_obj = Select(year_option)
    select_obj.select_by_index(17)

    time.sleep(2)

def facebook_radio_button_in_create_account():

    genders = driver.find_elements(By.XPATH, "//span[@data-type='radio']/span")
    print(len(genders))

    female_radio_button = driver.find_element(By.XPATH, "//input[@value='1']")
    male_radio_button = driver.find_element(By.XPATH, "//input[@value='2']")
    custom_radio_button = driver.find_element(By.XPATH, "//input[@value='-1']")

    get_first_name = "abcd"

    if get_first_name == "abcd":
        male_radio_button.click()
    else:
        print("invalid option")

    time.sleep(2)

def facebook_signup_option_in_create_account():
    signup_button = driver.find_element(By.NAME, "websubmit")
    signup_button.click()
    time.sleep(10)

def facebook_create_account_display():
    create_new_fb_account()
    facebook_dropdown_in_create_account()
    facebook_text_box_in_create_account()
    facebook_radio_button_in_create_account()
    facebook_signup_option_in_create_account()


# create_new_fb_account()
# facebook_dropdown_in_create_account()
# facebook_text_box_in_create_account()
# facebook_radio_button_in_create_account()
# facebook_signup_option_in_create_account()

facebook_create_account_display()
driver.close()



