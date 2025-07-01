import pytest
import os
from datetime import datetime
from selenium import  webdriver
from base.webdriver_factory import WebdriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', help='browser to execute automation code')
    parser.addoption("--headless", action='store', default=False, help='browser to execute automation code')


@pytest.fixture(scope="class")
def get_driver(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless = pytestconfig.getoption("headless")
    if browser and headless:
        wf = WebdriverFactory(browser, headless)
    elif browser:
        wf = WebdriverFactory(browser, headless=False)
    else:
        wf = WebdriverFactory('chrome', headless=False)
    driver = wf.get_driver_instance()
    driver.maximize_window()
    driver.get("https://www.goibibo.com/")
    request.cls.driver = driver
    yield
    driver.close()

def pytest_configure(config):
    logs_path = os.path.join(os.getcwd(), 'logs')
    if not os.path.exists(logs_path):
        os.mkdir(logs_path)
    unique_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    log_file_name = f"{unique_name}_execution.log"
    log_file_path = os.path.join(logs_path, log_file_name)
    config.option.log_file = log_file_path



