from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)


    def get_element(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        return element

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()


    def enter_text(self, locator, value):
        element = self.get_element(locator)
        element.send_keys(value)
