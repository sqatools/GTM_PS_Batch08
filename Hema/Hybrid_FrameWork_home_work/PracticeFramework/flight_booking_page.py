import time

from seleniumbase import SeleniumBase
from flight_booking_page_locator import *



class FlightBookingPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def close_icon(self):
        self.click_element(closeup_icon_locator)
    def notification_cancel(self):
        self.switch_iframe(iframe_prompt_locator)
        self.click_element(deny_button)
    def default_content_switch(self):
        self.switch_default()
    def select_source_city(self, city_name):
        self.click_element(source_city_locator)
        self.enter_text(source_city_input_locator, city_name)
        source_dropdown_locator = (By.XPATH, f"//span[contains(text(),'{city_name}')]")
        self.click_element(source_dropdown_locator)


    def select_dest_city(self, dest_city_name):
        self.enter_text(dest_city_input_locator, dest_city_name)
        dest_dropdown_locator = (By.XPATH, f"//span[contains(text(),'{dest_city_name}')]")
        self.click_element(dest_dropdown_locator)

    def select_departure_date(self, date_value):
        self.click_element(departure_date_arrow_locator)
        date_locator = (By.XPATH, f"//div[@aria-label='{date_value}']")
        self.click_element(date_locator)


    def select_travellers_details(self):
        self.click_element(traveller_dropdown_locator)
        self.click_element(adult_add_count_locator)
        self.click_element(children_add_locator)
        self.click_element(infant_add_locator)
        self.click_element(economy_locator)

    def click_done_button(self):
        self.click_element(done_button_locator)

    def search_button(self):
        self.click_element(search_flight_button_locator)

    def compare_close_button(self):
        self.click_element(got_it_locator)

    def okay_gotit(self):
        self.click_element(okay_gotit_locator)
    def get_filght_name(self):
        self.get_text(flight_name_locator)

    def fare_details(self):
        #list_fare = self.get_elements_list(view_fare_button_locator)
        list_fare = self.get_elements_list(view_fare_button_locator)
        #print(list_fare)
        print(len(list_fare))
        #self.click_elements_first(view_fare_button_locator)
        for fare in range(len(list_fare)):
            #print(fare)
            if fare == 2:
                print(fare)
                #fare_detail = self.get_element(list_fare)[fare]
                #(NOT WORKS) fare_detail = list_fare[fare]
                #Partial works:
                list_fare[2].click()
                #self.click_element(fare_detail)
                ## fare_detail.click()
                #self.driver.execute_script("arguments[0].scrollIntoView(true);", fare_detail)

                # Wait until it's clickable
                #self.wait(self.driver, 10).until(self.ec.element_to_be_clickable(fare_detail))

                #(NOT WORKS) self.get_elements_lists(fare_detail).click()
                #break
                #print(fare_text)
                #print(fare_detail)
                #self.click_element(fare_detail)

    def book_now(self):
        print("Next test case")
        time.sleep(5)
        self.click_element(fare_done_button)

    def user_consent(self):
        self.click_element(user_consent_locator)

    def summary(self):
        self.get_text(total_amount_fare_locator)
