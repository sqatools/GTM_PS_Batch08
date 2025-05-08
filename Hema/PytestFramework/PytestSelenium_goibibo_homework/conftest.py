import pytest
from selenium import webdriver
@pytest.fixture(scope='function')
def info_msg():
    print("----- Execution started --------")
    yield
    print("----- Execution completed ------")

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.cls.new_driver = driver
    yield
    driver.close()

