from base.sqa_automation.selenium_base import SeleniumBase
from .sqaautomationtools_page_locators import *



class SqaAutomationToolsPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def sqatoolsdummywebsite(self):
        self.log.info(f"dummy website")
        title = self.get_text(title_text_locator)
        print(title)

    def choose_option(self):
        self.log.warning(f"choose option")
        self.click_element(title_text_locator)

    def passenger_details(self, first_name, last_name, dob):
        self.log.warning(f"passenger details")
        self.click_element(first_name_input_locator)
        self.enter_text(first_name_input_locator, first_name)
        self.click_element(last_name_input_locator)
        self.enter_text(last_name_input_locator, last_name)
        self.click_element(dob_locator)
        self.enter_text(dob_locator, dob)
