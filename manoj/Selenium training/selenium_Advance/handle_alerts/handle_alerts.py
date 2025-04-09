import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://automationbysqatools.blogspot.com/2020/08/alerts.html")
alert = Alert(driver)

def handler_alert_box():
    driver.find_elements(By.ID, "btnshowMsg").click()
    print("Alert msg :", alert.text)
    time.sleep(2)
    alert.accept()

def handler_confirm_box():
    driver.find_elements(By.ID, "Button").click()
    print("confirm msg :", alert.text)
    time.sleep(2)
    alert.accept()
    msg = driver.find_elements(By.ID, "demo")
    assert msg.text == "You pressed OK!"
    print(msg.text)


    driver.find_elements(By.ID, "Button").click()
    print("confirm msg :", alert.text)
    time.sleep(2)
    alert.accept()
    msg = driver.find_elements(By.ID, "demo")
    assert msg.text == "You pressed cancel!"

    def handler_prompt_box():
        driver.find_elements(By.ID, "promptbtn").click()
        print("confirm msg :", alert.text)
        time.sleep(2)
        alert.send_keys("Harry")
        alert.accept()
        msg = driver.find_elements(By.ID, "prompt")
        assert msg.text == "Hello Harry potter! How are you"


# handler_alert_box()
# handler_confirm_box()
# handler_prompt_box()