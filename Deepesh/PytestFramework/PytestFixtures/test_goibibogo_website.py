from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.usefixtures("get_driver")
class TestGoibiboGO:

    def test_src_dest_city(self, request):
        print("Test Name :", request.node.name)
        self.new_driver.get("https://www.goibibo.com/")
        self.new_driver.find_element(By.XPATH, "//span[@class='logSprite icClose']").click()
        self.new_driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::p").click()
        self.new_driver.find_element(By.XPATH, "//span[text()='From']//following-sibling::input").send_keys("Mumbai")
        self.new_driver.find_element(By.XPATH, "//span[contains(text(), 'Mumbai, India')]").click()
        self.new_driver.find_element(By.XPATH, "//span[text()='To']//following-sibling::input").send_keys("Delhi")
        self.new_driver.find_element(By.XPATH, "//span[contains(text(), 'New Delhi, India')]").click()

    def test_select_depart_date(self, request):
        print("Test Name :", request.node.name)
        self.new_driver.find_element(By.XPATH, "//span[text()='Departure']//parent::div").click()
        self.new_driver.find_element(By.XPATH, "//div[contains(@aria-label,'Apr 30 2025')]").click()


    def test_select_travellers_flight_class(self, request):
        print("Test Name :", request.node.name)
        self.new_driver.find_element(By.XPATH, "//span[text()='Travellers & Class']//parent::div").click()
        # select no of adults.
        for _ in range(2):
            self.new_driver.find_element(By.XPATH, "//p[text()='Adults']//following-sibling::div/span[3]").click()

        for _ in range(2):
            self.new_driver.find_element(By.XPATH, "//p[text()='Children']//following-sibling::div/span[3]").click()

        for _ in range(2):
            self.new_driver.find_element(By.XPATH, "//p[text()='Infants']//following-sibling::div/span[3]").click()

        self.new_driver.find_element(By.XPATH, "//li[text()='premium economy']").click()
        self.new_driver.find_element(By.XPATH, "//a[text()='Done']").click()

        self.new_driver.find_element(By.XPATH, "//span[text()='SEARCH FLIGHTS']").click()
        time.sleep(10)








