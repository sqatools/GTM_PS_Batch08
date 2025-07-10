import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait( 10 )
driver.get( "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html" )


def select_num_of_pass():
    select_elem = driver.find_element( By.ID,"admorepass" )
    select_obj = Select( select_elem )
    select_obj.select_by_visible_text( "Add 2 more passenger (200%)" )
    time.sleep( 6 )


#select_num_of_pass()

def select_country():
    country_dropdown = driver.find_element(By.ID,"billing_country")
    country_obj = Select(country_dropdown)
    country_obj.select_by_value("AO")
    time.sleep(5)

select_country()