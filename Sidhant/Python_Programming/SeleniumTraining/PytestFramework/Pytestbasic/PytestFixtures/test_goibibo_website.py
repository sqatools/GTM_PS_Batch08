import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures( "get_driver" )
class Testgoibibo:
    def test_fligh_tbooking(self,request):
        print("Test Name:",request.node.name)
        self.new_driver.get( "https://www.goibibo.com/" )
        time.sleep( 4 )
        self.new_driver.find_element( By.XPATH, "//span[@role='presentation']" ).click()
        self.new_driver.find_element( By.XPATH, "//span[text() ='From']//following-sibling::p" ).click()
        self.new_driver.find_element( By.XPATH, "//span[text()='From']//following-sibling::input" ).send_keys( "Delhi" )
        self.new_driver.find_element( By.XPATH, "//span[contains(text(), 'New Delhi, India')]" ).click()
        time.sleep( 3 )
        self.new_driver.find_element( By.XPATH, "//span[text()='To']//following-sibling::input" ).send_keys( "Mumbai" )
        self.new_driver.find_element( By.XPATH, "//span[contains(text(), 'Mumbai, India')]" ).click()
        time.sleep( 5 )

    def test_select_depart_date(self,request):
        print( "Test Name:", request.node.name )
        self.new_driver.find_element( By.XPATH, "//span[text()='Departure']//parent::div" ).click()
        time.sleep( 5 )
        self.new_driver.find_element( By.XPATH, "//div[@aria-label='Wed Jun 04 2025']" ).click()
        time.sleep( 3 )

    def test_select_traveller_flight_class(self,request):
        print( "Test Name:", request.node.name )
        self.new_driver.find_element( By.XPATH,"//span[text()='Travellers & Class']//parent::div").click()
        for _ in range(2):
            self.new_driver.find_element(By.XPATH,"//p[text()='Adults']//following-sibling::div/span[3]").click()
            time.sleep(4)
            self.new_driver.find_element(By.XPATH, "//p[text()='Children']//following-sibling::div/span[3]").click()
            time.sleep(4)
        self.new_driver.find_element( By.XPATH,"//li[contains(text(),'premi')]").click()
        self.new_driver.find_element( By.XPATH, "//a[text()='Done']" ).click()
        time.sleep(3)

    def test_search_flight_butn(self,request):
        print( "Test Name:", request.node.name )
        self.new_driver.find_element( By.XPATH, "//span[text()='SEARCH FLIGHTS']//parent::div" ).click()
        time.sleep(5)