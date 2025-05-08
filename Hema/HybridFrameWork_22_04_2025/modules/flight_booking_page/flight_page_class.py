from base.selenium_base import SeleniumBase
from .flight_page_locators import *

class FlightPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.log.critical(f"pop up has to close")
        self.click_element(close_popup_icon)

    def select_source_city(self, source_city):
        self.log.warning(f"select source city :{source_city}")
        self.click_element(source_city_locator)
        self.enter_text(source_city_input, source_city)
        dropdown_locator = (By.XPATH, f"//span[contains(text(), '{source_city}')]")
        self.click_element(dropdown_locator)

    def select_dest_city(self, dest_city):
        self.log.warning(f"select dest city: {dest_city}")
        self.enter_text(dest_city_input, dest_city)
        dest_dropdown_locator = (By.XPATH, f"//span[contains(text(), '{dest_city}')]")
        self.click_element(dest_dropdown_locator)

    def select_travel_date(self, travel_date):
        self.log.critical(f"select travel date: {travel_date}")
        self.click_element(departure_data_locator)
        date_loc = (By.XPATH, f"//div[contains(@aria-label,'{travel_date}')]")
        self.click_element(date_loc)


