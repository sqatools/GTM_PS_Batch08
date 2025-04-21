import pytest
from selenium import webdriver
from modules.flight_booking_page.flight_booking_test_data import *

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()

