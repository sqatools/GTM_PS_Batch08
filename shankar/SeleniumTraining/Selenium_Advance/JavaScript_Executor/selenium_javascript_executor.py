import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
"""
driver.get("https://www.facebook.com")

website_url = driver.execute_script("return document.URL;")
website_title = driver.execute_script("return document.title;")
time.sleep(5)
print("website URL :", website_url)
print("website title :", website_title)

username = driver.execute_script("return document.getElementsByName('email')[0];")
username.send_keys("user1@gmail.com")

password = driver.execute_script("return document.getElementsByName('pass')[0];")
password.send_keys("admin@1234")
# https://www.w3schools.com/js/js_htmldom_events.asp
"""


driver.get("https://www.w3schools.com/js/default.asp")
# //h5[text()='Top References']

time.sleep(5)

# scroll by pixel
# driver.execute_script("window.scrollBy(0, 1000);")
#
# time.sleep(5)

# scroll to element by java script.
top_ref = driver.find_element(By.XPATH, "//h5[text()='Top References']")
driver.execute_script("arguments[0].scrollIntoView;", top_ref)

time.sleep(5)
driver.close()
