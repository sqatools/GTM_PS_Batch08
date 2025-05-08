from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
class SeleniumBase():

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

    def switch_iframe(self, locator):
        iframe_element = self.get_element(locator)
        self.driver.switch_to.frame(iframe_element)
        #return prompt_element

    def switch_default(self):
        self.driver.switch_to.default_content()

    def get_text(self, locator):
        element= self.get_element(locator).text
        return element

    def click_elements_first(self, locator):
        self.driver.find_elements(*locator)[0].click()
    def get_list_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def get_elements_list(self, locator, condition=ec.visibility_of_all_elements_located):
        elements_list = self.wait.until(condition(locator))
        return elements_list

    # def get_elements_lists(self, locator, condition=ec.element_to_be_clickable):
    #     elements_lists = self.wait.until(condition(locator))
    #     return elements_lists
