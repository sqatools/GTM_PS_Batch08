import logging
import os
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from utilities.utility_tools import Utils


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        self.log = logging.getLogger(__name__)
        self.util = Utils()

    def capture_screenshot(self, image_path=os.path.join(os.getcwd(), "logs/images")):
        if not os.path.exists(image_path):
            os.makedirs(image_path)
        file_name = f"{self.util.generate_unique_name()}.png"
        file_path = f"{image_path}/{file_name}"
        self.driver.save_screenshot(file_path)
        self.log.info(f"screenshot: {file_path}")

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
        elements_list = self.wait.until(condition(locator))
        return elements_list

    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            time.sleep(3)

            element.click()
        except Exception as e:
            self.log.debug(f"unable to click {e}")
            self.capture_screenshot()
            raise

    def enter_text(self, locator, value):
        try:
            self.log.info(f"enter text: {value} to element: {locator}")
            element = self.get_element(locator)
            element.clear()
            time.sleep(2)
            element.send_keys(value)

        except Exception as e:
            self.log.debug(f"unable to click {e}")
            self.capture_screenshot()
            raise

    def get_text(self, locator):
        try:
            element = self.get_element(locator)
            return element.text
        except Exception as e:
            self.log.debug(f"Unable to get element {e}")
            file_name = f"{self.util.generate_unique_name()}.png"
            file_path = f"logs/images/{file_name}"
            self.driver.save_screenshot(file_path)
            raise

    def select_dropdown_value(self, locator, value):
        try:
            self.log.info(f"select value: {value}from element: {locator}")
            element = self.get_element(locator)
            select = Select(element)
            select.select_by_visible_text(value)
            self.capture_screenshot()
        except Exception as e:
            self.log.debug(f"Unable to Click {e}")
            self.capture_screenshot()
            raise
