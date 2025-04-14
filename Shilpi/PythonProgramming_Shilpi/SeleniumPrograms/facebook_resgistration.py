from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
def click_create_new_account():
    time.sleep(3)
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    e1 = driver.find_element(By.XPATH, "//a[text()='Create new account']")
    time.sleep(3)
    e1.click()
    time.sleep(3)

def fill_name(fn,ln):
    firstname=driver.find_element(By.XPATH,"//input[@name='firstname']")
    time.sleep(3)
    firstname.send_keys(fn)
    time.sleep(3)
    lastname=driver.find_element(By.XPATH,"//input[@name='lastname']")
    lastname.send_keys(ln)
    time.sleep(3)

def birthday(month,day,year):
    m=driver.find_element(By.XPATH,"//select[@name='birthday_month']")
    time.sleep(2)
    select_month=Select(m)
    select_month.select_by_value(str(month))
    d=driver.find_element(By.XPATH,"//select[@name='birthday_day']")
    select_day=Select(d)
    time.sleep(2)
    select_day.select_by_value(str(day))
    time.sleep(2)
    y=driver.find_element(By.XPATH,"//select[@name='birthday_year']")
    select_year=Select(y)
    select_year.select_by_value(str(year))
    time.sleep(2)
    driver.quit()
def gender(g):
    g1=str(g)
    g1=g1.lower()
    if g1=="f" or g1=="female":
        gender=driver.find_element(By.XPATH,"//label[text()='Female']//following-sibling::input")
        gender.click()
    if g1=="m" or g1=="male":



click_create_new_account()
fill_name("Nutan","Durga")
birthday(3,3,1990)














