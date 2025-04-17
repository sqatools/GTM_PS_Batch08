import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

def select_num_of_pass():
    select_elem = driver.find_element(By.ID, "admorepass")
    select_obj = Select(select_elem)
    select_obj.select_by_visible_text("Add 2 more passenger (200%)")
    time.sleep(5)


def select_country():
    country_dropdown = driver.find_element(By.ID, "billing_country")
    sel_obj = Select(country_dropdown)
    #sel_obj.select_by_value("DZ")
    # index value will start from zero
    sel_obj.select_by_index(4)
    time.sleep(5)

#select_num_of_pass()
#select_country()

def select_dropdown(elem, value):
    sel_obj = Select(elem)
    sel_obj.select_by_visible_text(value)


def select_num_of_passengers():
    select_elem = driver.find_element(By.ID, "admorepass")
    select_dropdown(select_elem, "Add 2 more passenger (200%)")
    time.sleep(5)
    country_dropdown = driver.find_element(By.ID, "billing_country")
    select_dropdown(country_dropdown, "India")

select_num_of_passengers()

# Home work
# automate create facebook acount to pratice dropdown
