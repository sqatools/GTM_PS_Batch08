import logging
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from Hema.HybridFrameWork_04_05_2025.utilities.utility_tools import Utils

class SeleniumBase:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        self.log = logging.getLogger(__name__)
        self.util = Utils()

    def capture_screenshot(self, image_path=os.path.join(os.getcwd(), "logs/images")):
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        file_name = f"{self.util.generate_unique_name()}.png"
        filepath = f"{image_path}/{file_name}"
        self.driver.save_screenshot(filepath)
        self.log.info(f"screenshot: {filepath}")

    def get_element(self, locator, condition=ec.presence_of_element_located):
        try:
            self.log.info(f"finding element: {locator}")
            element = self.wait.until(condition(locator))
            return element
        except Exception as e:
            self.log.debug(f"Unable to find element {e}")
            self.capture_screenshot()
            raise

    def get_elements_list(self, locator, condition=ec.presence_of_all_elements_located):
        try:
            self.log.info(f"getting element list: {locator}")
            element_list = self.wait.until(condition(locator))
            return element_list
        except Exception as e:
            self.log.debug(f"Unable to find element list {e}")
            self.capture_screenshot()
            raise


    def click_element(self, locator):
        try:
            self.log.info(f"clicking element {locator}")
            element = self.get_element(locator)
            element.click()
        except Exception as e:
            self.log.debug(f"Unable to click element: {e}")
            self.capture_screenshot()
            raise


    def enter_text(self, locator, value):
        try:
            self.log.info(f"entering text: {value} to element: {locator}")
            element = self.get_element(locator)
            element.clear()
            element.send_keys(value)

        except Exception as e:
            self.log.debug(f"Unable to enter text: {e}")
            self.capture_screenshot()
            raise

    def get_text(self, locator):
        try:
            self.log.info(f"getting text from element: {locator}")
            element = self.get_element(locator)
            return element.text

        except Exception as e:
            self.log.debug(f"Unable to get text: {e}")
            file_name = f"{self.util.generate_unique_name()}.png"
            filepath = f"logs/images/{file_name}"
            self.driver.save_screenshot(filepath)
            raise

    def select_dropdown(self, locator, value):
        try:
            self.log.info(f"select value: {value} from element: {locator}")
            element = self.get_element(locator)
            select = Select(element)
            select.select_by_visible_text(value)

        except Exception as e:
            self.log.debug(f"Unable to select dropdown: {e}")
            self.capture_screenshot()
            raise
