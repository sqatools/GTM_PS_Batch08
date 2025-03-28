"""
# use below command to install selenium
pip install selenium
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FACEBOOK_URL = 'https://www.facebook.com'
CONSTANT_URL = 'https://www.facebook.com/r.php?entry_point=login'

def initialize_driver():
    ## Initialize the Browser ##
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def login_facebook(driver,email,password):
    ## Login to FaceBook Account ##
    driver.get(FACEBOOK_URL)
    driver.find_element(By.ID,"email").send_keys(email)
    driver.find_element(By.NAME,"pass").send_keys(password)
    # driver.find_element(By.NAME,"login").click()

def navigate_to_create_account(driver):
    ### Navigates to the 'Create New Account' page. ###
    try:
        # Wait until the 'Create New Account' link is clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Create new account"))
        ).click()
    except TimeoutException:
        print("Failed to navigate to the 'Create New Account' page.")
        driver.quit()

def create_new_account(driver):
    try:
        ### Wait for the registration page to load  ###
        WebDriverWait(driver, 10).until(
            EC.url_to_be(CONSTANT_URL)
        )

        driver.find_element(By.NAME,"firstname").send_keys("Sheetal")
        driver.find_element(By.NAME,"lastname").send_keys("S")
        driver.find_element(By.ID,"day").send_keys(27)
        driver.find_element(By.ID, "month").send_keys("Mar")
        driver.find_element(By.ID,"year").send_keys(2024)
        # driver.find_element(By.XPATH,"//input[@type='radio' and @value= '1']").click()
        driver.find_element(By.XPATH, "(//input)[@type='radio'][2]").click()
        driver.find_element(By.NAME,"reg_email__").send_keys(9999977665)
        driver.find_element(By.ID,"password_step_input").send_keys("user2")


    except NoSuchElementException as e:
        print(f"The required text is not found : {e}")

    except TimeoutException:
        print("Timeout: Page did not load in time.")
        driver.quit()


def main():
    driver = initialize_driver()
    try:
        login_facebook(driver, 'user1@gmail.com', 'user1')
        navigate_to_create_account(driver)
        create_new_account(driver)
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
