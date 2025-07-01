from base.selenium_base import SeleniumBase
from .flight_booking_locators import *


class FlightBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_login_popup(self):
        self.log.info("closing login popup")
        self.click_element(close_popup_loc)

    def enter_source_city(self, city_name):
        self.log.info(f"entering source city name: {city_name}")
        self.click_element(source_city_label)
        self.enter_text(source_city_field, city_name)
        src_city_name = (By.XPATH, f"//span[contains(text(), '{city_name}')]")
        self.click_element(src_city_name)

    def enter_dest_city(self, city_name):
        self.log.info(f"entering dest city name: {city_name}")
        self.enter_text(dest_city_field, city_name)
        dest_city_name = (By.XPATH, f"//span[contains(text(), '{city_name}')]")
        self.click_element(dest_city_name)

    def select_depart_date(self, deprt_date):
        self.log.info(f"selected departure date: {deprt_date}")
        self.click_element(depart_date_label)
        depart_date_value = (By.XPATH, f"//div[contains(@aria-label,'{deprt_date}')]")
        self.click_element(depart_date_value)
