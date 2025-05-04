# https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

Current_URL = "https://www.facebook.com/login/?next=https%3A%2F%2Fwww.facebook.com%2F"

class Driver_Initialize:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Current_URL)

class Login_UI_Validation:

    def __init__(self,driver):
        self.driver = driver
        # super().__init__()

    def url_validation(self):
        # driver = self.initialize_driver()

        url_name = self.driver.current_url
        print(f"Current URL is: {url_name}")
        time.sleep(3)

        try:
            element = self.driver.find_element(By.XPATH, "//div[@class = 'login_form_container']")
            print(f"Element found: {element.text}")
        except Exception as e:
            print(f"Error: {str(e)}")


class Register_User:

    def __init__(self, driver):
        self.driver = driver

    def action_on_signup(self):
        self.action = ActionChains(self.driver)
        self.First_option = self.driver.find_element(By.XPATH,"//div[@id = 'login_link']//a[text() = 'Sign up for Facebook']")
        self.action.move_to_element(self.First_option).click().perform()
        # assert "Sign up" in self.First_option

    def signup_page_validation(self):

        try:
                signup_page = self.driver.current_url
                print(f"Current URL is: {signup_page}")
                sigup_link = self.driver.find_element(By.XPATH, "//div[text() = 'Create a new account']")
                self.header = By.XPATH, "//div[text() = 'Create a new account']"
                WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.header ))

                # assert "Create" in sigup_link

        except NoSuchElementException as e:
                print(f"The required text is not found : {e}")

        except TimeoutException:
                print("Timeout: Page did not load in time.")

    def create_new_account(self):

        self.driver.find_element(By.NAME, "firstname").send_keys("Sheetal")
        self.driver.find_element(By.NAME, "lastname").send_keys("S")
        self.driver.find_element(By.ID, "day").send_keys(27)
        self.driver.find_element(By.ID, "month").send_keys("Mar")
        self.driver.find_element(By.ID, "year").send_keys(2024)
        # driver.find_element(By.XPATH,"//input[@type='radio' and @value= '1']").click()
        self.driver.find_element(By.XPATH, "(//input)[@type='radio'][2]").click()
        self.driver.find_element(By.NAME, "reg_email__").send_keys(9999977665)
        self.driver.find_element(By.ID, "password_step_input").send_keys("user2")

    def back_to_Login(self):
        self.driver.back()


class Login_TestCase:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_firstelement(self):
        self.First_option = self.driver.find_element(By.XPATH,"")


    def select_and_add_value(self,uname,passwd):
        # username = "Amit@gmail.com"
        # passwd = "Sharma"

        self.uname = self.driver.find_element(By.XPATH,"//div//input[@name= 'email']").send_keys(uname)
        self.passwd = self.driver.find_element(By.XPATH,"//div//input[@name= 'pass']").send_keys(passwd)
        self.driver.find_element(By.XPATH,"//button[@id = 'loginbutton']").click()

    def driver_close(self):
        self.driver.quit()

class Main:

    def __init__(self):
        self.driver_init = Driver_Initialize()
        self.driver = self.driver_init.driver
        self.login_UI = Login_UI_Validation(self.driver)
        self.reg_user = Register_User(self.driver)
        self.login_TC = Login_TestCase(self.driver)

    def run(self):
        self.login_UI.url_validation()
        self.reg_user.action_on_signup()
        self.reg_user.signup_page_validation()
        self.reg_user.create_new_account()
        self.reg_user.back_to_Login()
        self.login_TC.select_and_add_value("Sheetal@gmail.com","sheetal")
        self.login_TC.driver_close()
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    main_program = Main()
    main_program.run()

