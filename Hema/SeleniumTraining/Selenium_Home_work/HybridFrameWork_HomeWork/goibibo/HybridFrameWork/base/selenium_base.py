from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=timeout)

    def get_element(self, locator, condition=ec.presence_of_element_located):
        element = self.wait.until(condition(locator))
        return element

    def get_elements(self, locator, condition=ec.presence_of_all_elements_located):
        element_list = self.wait.until(condition(locator))
        return element_list

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def enter_text(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text
    def select_dropdown_element(self, locator,value):
        element = self.get_element(locator)
        select = Select(element)
        select.select_by_visible_text(value)
        #select.select_by_value(value)
        #select.select_by_index(value)

