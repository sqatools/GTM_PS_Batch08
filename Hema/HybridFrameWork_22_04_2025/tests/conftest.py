import pytest
from selenium import webdriver
from modules.flight_booking_page.flight_booking_test_data import *
from utilities.utility_tools import Utils

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_configure(config):
    util = Utils()
    unique_name = util.generate_unique_name()
    #  f"execution_22_04_25_22_10_58.log"
    log_file_name = f"execution_{unique_name}.log"
    log_file_path = f"logs/{log_file_name}"
    # logs/execution_22_04_25_22_10_58.log
    config.option.log_file = log_file_path
