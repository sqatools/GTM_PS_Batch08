from base.selenium_base import SeleniumBase
from .flight_page_locator import *
import time


class FlightPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.log.critical(f"pop up has to close")
        self.click_element(close_popup_icon)

    def close_popup_second(self):
        self.log.warning(f"second popup has to be close")
        self.click_element(close_popup_icon1)

    def select_source_city(self, source_city):
        self.log.warning(f"select source city: {source_city}")
        self.click_element(source_city_locator)
        self.enter_text(source_city_input, source_city)
        dropdown_locator = (By.XPATH, f"//span[contains(text(), '{source_city}')]")
        self.click_element(dropdown_locator)

    def select_dest_city(self, dest_city):
        self.log.warning(f"select dest.city: {dest_city}")
        self.click_element(dest_city_locator)
        self.enter_text(dest_city_input, dest_city)
        dest_dropdown_locator = (By.XPATH, f"//span[contains(text(), '{dest_city}')]")
        self.click_element(dest_dropdown_locator)

    def select_travel_date(self, travel_date):
        self.log.critical(f"select travel date: {travel_date}")
        # self.click_element(departure_data_locator)
        # time.sleep(5)
        date_location = (By.XPATH, f"//div[contains(@aria-label, '{travel_date}')]")
        time.sleep(5)
        self.click_element(departure_data_locator)
        time.sleep(5)
        self.click_element(date_location)

    def select_Travel_and_class(self, adults):
        self.log.warning(f"select travel and class: ")
        self.click_element(travel_class_loc)
        time.sleep(5)
        self.click_element(flight_class_loc)
        time.sleep(5)
        self.click_element((By.XPATH, f"//p[@data-cy='adultRange']//following::ul/li[@data-cy='{adults}']"))
        time.sleep(3)
        self.click_element(Apply_btn_loc)
        time.sleep(4)

    def search_btn_All(self):
        self.log.critical("Bus Booking Testing")
        self.click_element(search_btn_loc)
        time.sleep(4)

    def login_to_student_website(self, username, password):
        self.enter_text(username_field, username)
        self.enter_text(password_field, password)
        self.click_element(submit_btn)
        head_text = self.get_text(success_msg_loc)
        assert head_text == "Logged In Successfully"

    def bus_booking_start(self):
        self.click_element(bus_btn_loc)
        time.sleep(3)

    def select_bus_source_city(self, source_city):
        self.log.warning(f"Enter the bus source location: {source_city}")
        self.click_element(bus_source_loc)
        time.sleep(4)
        self.enter_text(bus_source_loc, source_city)
        dropdown_locator = (By.XPATH, f"//span[contains(normalize-space(.), '{source_city}')]")
        self.click_element(dropdown_locator)

    def select_bus_destin_city(self, dest_city):
        self.log.warning(f"Enter the bus source location: {dest_city}")
        self.click_element(bus_dest_loc)
        time.sleep(4)
        self.enter_text(bus_dest_loc, dest_city)
        dropdown_locator = (By.XPATH, f"//span[contains(normalize-space(.), '{dest_city}')]")
        self.click_element(dropdown_locator)

    def bus_travel_date(self, depart_date):
        self.click_element(bus_select_date)
        time.sleep(5)
        date_loc = (By.XPATH, f"//span[text()='{depart_date}']//parent::li")
        self.click_element(date_loc)
        time.sleep(5)
        self.click_element(bus_search_btn)
        time.sleep(5)





