# import os
# import sys
#
#
# current_file_dir = os.path.dirname(__file__)
#
#
# project_root = os.path.abspath(os.path.join(current_file_dir, '..', '..'))
#
#
# sys.path.append(project_root)
# print("Project root added to path:", project_root)
#
# # Now you can import from base_package
#
from base_package.selenium_base import SeleniumBase
from .bus_page_locator import *

class BusPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        print("Hello World")

    def close_popup(self):
        self.click_element(close_popup_icon)

    def bus_loc_click(self):
        self.click_element(bus_location_icon)

    def select_source_city(self, source_city):
        self.click_element(source_city_input)
        self.enter_text(source_city_input, source_city)
        dropdown_locator = (By.XPATH, f"//span[contains(text(), '{source_city}')]")
        self.click_element(dropdown_locator)

    def select_dest_city(self, dest_city):
        self.enter_text(dest_city_input, dest_city)
        dest_dropdown_locator = (By.XPATH, f"//span[contains(text(), '{dest_city}')]")
        self.click_element(dest_dropdown_locator)

