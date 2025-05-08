from base.selenium_base import SeleniumBase
from .flight_page_locator import *

class FlightPageBase(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.click_element(close_popup_icon)


    def source_city(self, source_city):
        self.click_elenent(source_city_locator)
        self.enter_text(source_city_input, source_city)
        dropdown_locator = (By.XPATH, f"//li[@role='presentation']//following::span[contains(text(),'{source_city}')]")
        self.click_element(dropdown_locator)

    def destination_city(self, dest_city):
        self.enter_text(dest_city_input, dest_city)
        dest_dropdown_locator = (By.XPATH, f"//li[@role='presentation']//following::span[contains(text(),'{dest_city}')]")
        self.click_element(dest_dropdown_locator)

    def date_drodown(self, departure_date_dropdown):
        self.click_element(departure_date_locator)
        self.click
