import time
from selenium import webdriver

browser = "fireFox" \
          ""
if browser.lower() == "chrome":
    driver = webdriver.Chrome()
elif browser.lower() == "firefox":
    driver = webdriver.Firefox()
elif browser.lower() == "edge":
    driver = webdriver.Edge()

driver.maximize_window()
driver.implicitly_wait( 10 )

driver.get( "https://www.facebook.com" )
time.sleep( 5 )
driver.close()
