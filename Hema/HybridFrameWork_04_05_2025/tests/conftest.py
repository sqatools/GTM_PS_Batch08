import pytest
from selenium import webdriver
from Hema.HybridFrameWork_04_05_2025.modules.sqaautomationtoolspage.sqaautomationtools_test_data import *
from Hema.HybridFrameWork_04_05_2025.utilities.utility_tools import Utils
from Hema.HybridFrameWork_04_05_2025.base.sqa_automation.webdriver_factory import WebdriverFactory
import os

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default="chrome", help="browser to execute code")
    parser.addoption("--headless", action='store', default=False, help="GUI execution mode")

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(sqaautomationtools_url)
    request.cls.driver = driver
    yield
    driver.close()
@pytest.fixture(scope='class')
def get_driver_sqaautomation(request, pytestconfig):
    browser = pytestconfig.getoption("browser")
    headless_value = pytestconfig.getoption("headless")
    wf = WebdriverFactory(browser, headless=headless_value)
    driver = wf.get_driver_instance()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(sqaautomationtools_url)
    request.cls.driver = driver
    yield
    driver.close()
def pytest_configure(config):
    util = Utils()
    unique_name = util.generate_unique_name()
    log_path=os.path.join(os.getcwd(), 'logs')

    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file_name = f"execution_{unique_name}.log"
    log_file_path = f"{log_path}/{log_file_name}"
    config.option.log_file = log_file_path