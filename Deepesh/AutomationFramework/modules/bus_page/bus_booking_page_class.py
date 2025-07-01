from base.selenium_base import SeleniumBase
from .bus_booking_page_data import *
from .bus_booking_page_locator import *


class BusBooking(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver=driver)

    def goto_bus_booking_page(self):
        self.log.info(f"Open URL: {bus_booking_url}")
        self.driver.get(bus_booking_url)

    def select_from_city(self, src_city):
        self.log.info(f"select source city: {src_city}")
        self.enter_text(from_city_input_field, src_city)
        src_city_label = (By.XPATH, f"//span[text()='{src_city}']//parent::li")
        self.click_element(src_city_label)

    def select_dest_city(self, dest_city):
        self.log.info(f"select dest city: {dest_city}")
        self.enter_text(dest_city_input_field, dest_city)
        dest_city_label = (By.XPATH, f"//span[text()='{dest_city}']//parent::li")
        self.click_element(dest_city_label)

    def select_depart_date(self, depart_date):
        self.log.info(f"select depart date: {depart_date}")
        self.click_element(booking_date_loc)
        date_label = (By.XPATH, f"//span[text()='{depart_date}']//parent::li")
        self.click_element(date_label)

    def click_search_button(self):
        self.log.info(f"click to search button")
        self.click_element(search_btn)

    def select_bus(self, bus_name):
        self.log.info("Selecting bus to book the seat")
        select_bus_dynmc = (By.XPATH, f"(//p[text()='{bus_name}']//parent::div//parent::div//span[text()='SELECT SEAT'])[1]")
        self.click_element(select_bus_dynmc)

    def select_boarding_point(self, boarding_loc):
        self.log.info(f"Selecting boarding point : {boarding_loc}")
        boarding_point = (
        By.XPATH, f"//p[text()='Boarding Point']//parent::div//p[text()='{boarding_loc}']//ancestor::label/label")
        self.click_element(boarding_point)

    def select_dropping_point(self, drop_loc):
        self.log.info(f"Selecting dropping point : {drop_loc}")
        dropping_point = (
        By.XPATH, f"//p[text()='Dropping Point']//parent::div//p[text()='{drop_loc}']//ancestor::label/label")
        self.click_element(dropping_point)

    def select_seat(self, first_avail_seat=1):
        self.log.info(f"Selecting 1st available sleeper seat")
        seat_xpath = (By.XPATH,
                      f"(//span[text()='UPPER']//ancestor::div[contains(@class, 'BusBerthstyles')]//*[contains(@class, 'BusSleeperIcon')])[{first_avail_seat}]")
        self.click_element(seat_xpath)

    def click_to_continue_button(self):
        self.click_element(continue_button)

    def enter_passenger_details(self, name, age, email, phone, address,
                                pincode, state_name, flight_type, gender='male'):
        self.enter_text(name_field_loc, name)
        self.enter_text(age_field_loc, age)
        if gender.lower() == 'male':
            self.click_element(male_gender)
        elif gender.lower() == 'female':
            self.click_element(female_gender)
        self.enter_text(email_field, email)
        self.enter_text(phone_number_field, phone)
        self.enter_text(billing_Address, address)
        self.enter_text(billing_pincode, pincode)
        self.click_element(state_dropdown)
        state_name_dynmc = (By.XPATH, f"//li[text()='{state_name}']")
        self.click_element(state_name_dynmc)
        flight_type_radio_button = (By.XPATH, f"//span[text()='{flight_type}']//preceding-sibling::span")
        self.click_element(flight_type_radio_button)

    def add_promo_code(self, promo_code):
        self.enter_text(promo_field, promo_code)
    def click_to_pay_button(self):
        self.click_element(pay_button)
