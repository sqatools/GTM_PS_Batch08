import pytest
from selenium import webdriver


@pytest.fixture( scope='function' )
def info_msg():
    print( "\n--execution started--" )
    yield
    print( "\n--execution completed--" )


@pytest.fixture(scope = 'class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.new_driver = driver   #request is inbuilt api
    yield
    driver.close()
