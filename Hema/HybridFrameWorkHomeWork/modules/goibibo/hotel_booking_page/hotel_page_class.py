from Hema.HybridFrameWorkHomeWork.base.selenium_base import SeleniumBase
from .hotel_page_locators import *

class HotelPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_popup(self):
        self.log.critical(f"popup has to close")
        self.click_element(close_popup_icon)

    def select_location(self, where_to):
        self.log.warning(f"select location: {where_to}")
        self.click_element(where_to_locator)
        self.enter_text(where_to_input, where_to)
        where_to_dropdown_locator = (By.XPATH, f"//p[text()='Popular Searches']//ancestor::ul/li//following::p[text()='Goa']")
        self.click_element(where_to_dropdown_locator)

    def select_checkin_date(self, checkin_date):
        self.log.critical(f"select checkin travel date: {checkin_date}")
        self.click_element(checkin_locator)
        checkin_date_loc = (By.XPATH, f"//li[@class='date_is_selectable_true' and @data-testid='date_li_{checkin_date}')]")
        self.click_element(checkin_date_loc)

    def select_checkout_date(self, checkout_date):
        self.log.critical(f"select checkout travel date: {checkout_date}")
        self.click_element(checkout_locator)
        checkout_date_loc = (By.XPATH, f"//li[@class='date_is_selectable_true' and @data-testid='date_li_{checkout_date}')]")
        self.click_element(checkout_date_loc)

    def click_guest_room(self):
        #self.log.warning(f"select guest room: {}")
        self.click_element(guest_room_locator)

    def select_room_count(self, room_count):
        room_add_loc = (By.XPATH, f"//span[contains(text(), 'Rooms')]//parent::div//following-sibling::div//following-sibling::h4[text()='{room_count}']")
        self.click_element(room_add_loc)

    def select_adult_count(self, adult_count):
        adult_add_loc = (By.XPATH, f"//span[contains(text(), 'Adults')]//parent::div//following-sibling::div//following-sibling::h4[text()='{adult_count}']")
        self.click_element(adult_add_loc)

    def select_child_count(self, child_count):
        child_add_loc = (By.XPATH, f"//span[contains(text(), 'Adults')]//parent::div//following-sibling::div//following-sibling::h4[text()='{child_count}']")
        self.click_element(child_add_loc)

    def done_option(self):
        self.click_element(done_button_locator)


    def search_click(self):
        self.click_element(search_button_locator)

