from selenium_base import SeleniumBase
from flight_booking_page_locator import *


# Page class and setup inheritance between page class and SeleniumBase class.
class FlightBookingPage(SeleniumBase):
    """
    When we setup inheritance between two classes, then we can initiate the parent constructor
    in the child class with the help of super keyword
    """

    def __init__(self, driver):
        super().__init__(driver)

    def close_singup_popup(self):
        self.click_element(close_up_icon_locator)

    def select_source_city(self, city_name):
        self.click_element(source_city_locator)
        self.enter_text(source_city_input, city_name)
        dropdown_locator = (By.XPATH, f"//span[contains(text(), '{city_name}')]")
        self.click_element(dropdown_locator)

    def select_dest_city(self, dest_city):
        self.enter_text(dest_city_input, dest_city)
        dest_dropdown_locator = (By.XPATH, f"//span[contains(text(), '{dest_city}')]")
        self.click_element(dest_dropdown_locator)
