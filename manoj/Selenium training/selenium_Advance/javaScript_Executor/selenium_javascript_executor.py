import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.facebook.com")

website_url = driver.execute_script("return document.URL")
website_title = driver.execute_script("return document title")
time.sleep(15)
print("website URL :", website_url)
print("website title :", website_title)

username = driver.execute_script("document.getElementByName('email');")
username.send_keys("user1@gmail.com")

password = driver.execute_script("document.getElementByName('pass');")
password.send_keys("admin@12345")


driver.find_element("https;//www.w3schools.com/js/default.asp")
# //h5[text()='Top References']

driver.execute_script("window.scrollBy(0, 1000);")
time.sleep(5)

top_ref = driver.find_elements(By.XPATH, "//h5[text()='Top References'];")
driver.execute_script("arguments[0].scrollIntoView;", top_ref)

time.sleep(5)
driver.close()
