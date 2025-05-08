import time

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('get_driver')
class Test_Goibibo_site:

    def test_flight_booking(self, request):
        print("Testcase name: ", request.node.name)

        self.new_driver.get("https://www.goibibo.com/flights/")
        self.new_driver.find_element(By.XPATH, "//span[@role='presentation']").click()
        time.sleep(5)

    def test_round_trip(self):

        round_trip = self.new_driver.find_element(By.XPATH, "//p[text()='Round-trip']//parent::li/span")
        round_trip.click()

        from_field = self.new_driver.find_element(By.XPATH, "//p[text()='Enter city or airport']")
        from_field.click()

        from_input_field = self.new_driver.find_element(By.XPATH, "//span[text()='From']//parent::div//following-sibling::input[@type='text']")
        from_input_field.send_keys("Chennai")

        from_values = self.new_driver.find_elements(By.XPATH, "//span[text()='Chennai, India']//ancestor::ul/li")
        list_from_value=[]
        for value in from_values:
            list_from_value.append(value.text)
        print(list_from_value)
        from_value = self.new_driver.find_element(By.XPATH, "//span[text()='Chennai, India']//ancestor::ul/li[1]")

        #if from_value in list_from_value:
        from_value.click()
        time.sleep(5)

        to_field = self.new_driver.find_element(By.XPATH, "//p[text()='Enter city or airport']")
        to_field.click()

        time.sleep(2)

        to_input_field = self.new_driver.find_element(By.XPATH, "//span[text()='To']//parent::div//following-sibling::input[@type='text']")
        to_input_field.send_keys("Bangalore")

        to_value = self.new_driver.find_element(By.XPATH, "//span[text()='Bengaluru, India']//ancestor::ul/li")
        to_value.click()
        time.sleep(5)
        departure = self.new_driver.find_element(By.XPATH, "//span[text()='Departure']//following-sibling::p[1]")
        departure.click()

        time.sleep(15)



