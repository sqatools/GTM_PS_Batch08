import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver.implicitly_wait(10)
    driver.get("https://www.goibibo.com")
    request.cls.driver = driver
    yield
    driver.close()