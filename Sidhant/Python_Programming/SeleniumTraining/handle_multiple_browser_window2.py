import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

topics_list =['Software Testing Principles','Grey Box Testing','White Box Testing']
count =1
for topic in topics_list:
    driver.find_element( By.LINK_TEXT, topic).click()
    window_list = driver.window_handles
    time.sleep( 5 )
    driver.switch_to.window( window_list[1] )
    driver.save_screenshot( f"new_window_{count}.png" )

    # verify header element

    header_line = driver.find_element( By.XPATH, '//h3[@itemprop="name"]' )
    print( "the line:", header_line )
    # close new tab
    driver.close()
    time.sleep( 5 )
    driver.switch_to.window( window_list[0] )
    driver.save_screenshot( "homepage.png" )
    count +=1
time.sleep( 3 )
driver.close()


