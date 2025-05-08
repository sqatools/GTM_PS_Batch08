# https://automationbysqatools.blogspot.com/2021/05/dummy-website.html
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.driver import ChromeDriver

Current_URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"

class Booking_driver_Initialize:

    def __init__(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Current_URL)

class Booking_UI_Validation:

    def __init__(self,driver):
        self.driver = driver
        # super().__init__()

    def input_value(self):
        # driver = self.initialize_driver()

        url_name = self.driver.current_url
        print(f"Current URL is: {url_name}")
        time.sleep(3)

        try:
            element = self.driver.find_element(By.XPATH, "//h1")
            print(f"Element found: {element.text}")
        except Exception as e:
            print(f"Error: {str(e)}")
        # finally:
        #     self.driver.quit()

class Bookin_field_check:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_firstelement(self):
        self.First_option = self.driver.find_element(By.XPATH,"//h3[text()='Choose the correct option:']")

    def action_fun(self):
        self.action = ActionChains(self.driver)
        self.action.send_keys_to_element(self.First_option).perform()
        assert "correct" in self.First_option.text

    def select_and_add_value(self,fname,lname,DOB):
        firtname = "Amit"
        lastname = "Sharma"
        self.sel = self.driver.find_element(By.XPATH,"//h3[text()='Choose the correct option:']//following-sibling::div//li[5]//input")
        self.sel.click()
        self.fname = self.driver.find_element(By.XPATH,"//div//h2[text() = 'Passenger Details']//..//div[2]//input[@type='text'][1]").send_keys(firtname)
        self.lname = self.driver.find_element(By.XPATH,"//div//h2[text() = 'Passenger Details']//..//div[2]//input[@type='text'][2]").send_keys(lastname)
        self.dob = self.driver.find_element(By.ID,"birthday").send_keys("04/11/1992")




class Main:

    def __init__(self):
        self.booking_driver = Booking_driver_Initialize()
        self.driver = self.booking_driver.driver
        self.ui_validation = Booking_UI_Validation(self.driver)
        self.book_fields = Bookin_field_check(self.driver)

        # self.booking_driver = Booking_driver_Initialize()
        self.ui_validation = Booking_UI_Validation(self.driver)
        self.book_fields = Bookin_field_check(self.driver)

    def run(self):
        self.ui_validation.input_value()
        self.book_fields.scroll_to_firstelement()
        self.book_fields.action_fun()
        self.book_fields.select_and_add_value("Mohit", "B", "05/11/1995")
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    main_program = Main()
    main_program.run()

