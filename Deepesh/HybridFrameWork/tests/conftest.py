import pytest
from selenium import webdriver
from modules.flight_booking_page.flight_booking_test_data import *
from utilities.utility_tools import Utils
from base.webdriver_factory import WebdriverFactory
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="chrome", help="browser to execute code")
    parser.addoption("--headless", action='store', default=False, help="GUI execution mode")
    parser.addoption("--username", action='store', default='student', help="GUI execution mode")
    parser.addoption("--password", action='store', default='Password123', help="GUI execution mode")


@pytest.fixture(scope="function")
def get_user_cred(pytestconfig):
    username = pytestconfig.getoption("username")
    password = pytestconfig.getoption("password")
    return username, password


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope='class')
def get_driver_goibibo(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless_value = pytestconfig.getoption("headless")
    wf = WebdriverFactory(browser, headless=headless_value)
    driver = wf.get_driver_instance()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(goibibo_url)
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope='class')
def get_driver_facebook(request):
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
    log_path=os.path.join(os.getcwd(), "logs")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file_name = f"execution_{unique_name}.log"
    log_file_path = f"{log_path}/{log_file_name}"
    # logs/execution_22_04_25_22_10_58.log
    config.option.log_file = log_file_path
