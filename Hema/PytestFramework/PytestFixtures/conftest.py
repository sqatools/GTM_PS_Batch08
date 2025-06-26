import pytest
from selenium import webdriver


"""
-> when defined any fixture function in conftest.py file, then not need to import the conftest file
   in the test file, to call fixture function.
->  It will auto import in all the test files internally.

"""
@pytest.fixture(scope='function')
def info_msg(request):
    print("Test Name :", request.node.name)
    print("\n--execution started ----")
    yield
    print(" \n --execution completed ----")


@pytest.fixture(scope='class')
def get_driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.new_driver = driver
    yield
    driver.close()

