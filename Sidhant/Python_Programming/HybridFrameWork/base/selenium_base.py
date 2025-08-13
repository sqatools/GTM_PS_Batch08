from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import logging


class SeleniumBase:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait( self.driver, timeout=timeout )
        self.log = logging.getLogger( __name__ )

    def get_element(self, locator, condition=ec.presence_of_element_located):
        try:
            self.log.info( f"finding element: {locator}" )
            element = self.wait.until( condition( locator ) )
            return element
        except Exception as e:
            self.log.debug(f"Unable to find element {e}")




    def get_elements_list(self, locator, condition=ec.presence_of_all_elements_located):
        elements_list = self.wait.until( condition( locator ) )
        return elements_list

    def click_element(self, locator):
        try:
            element = self.get_element( locator )
            element.click()
        except Exception as e:
            self.log.debug(f"unable to click {e}")



    def enter_text(self, locator, value):
        self.log.info( f"enter text :{value} to element:{locator}" )
        element = self.get_element( locator )
        element.send_keys( value )

    def get_text(self, locator):
        try:
            element = self.get_element( locator )
            return element.text
        except Exception as e:
            self.log.debug(f"Unable to get element {e}")
    def select_dropdown_value(self, locator, value):
        self.log.info(f"select value:{value}from element:{locator}")
        element = self.get_element( locator )
        select = Select( element )
        select.select_by_visible_text( value )
