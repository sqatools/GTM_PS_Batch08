import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
alert = Alert(driver)

def handler_alert_box():
    driver.find_element(By.ID, "btnShowMsg").click()
    print("Alert msg :", alert.text)
    time.sleep(2)
    alert.accept()

def handler_confirm_box():
    driver.find_element(By.ID, "button").click()
    print("confirm msg :", alert.text)
    time.sleep(2)
    alert.accept()
    msg = driver.find_element(By.ID, "demo")

    assert msg.text == "You pressed OK!"
    print(msg.text)

    driver.find_element(By.ID, "button").click()
    time.sleep(2)
    alert.dismiss()
    msg_elem = driver.find_element(By.ID, "demo")
    assert msg_elem.text == "You pressed Cancel!"
    print(msg.text)


def handler_prompt_box():
    driver.find_element(By.ID, "promptbtn").click()
    time.sleep(2)
    input_val = "GTM"
    alert.send_keys(input_val)
    alert.accept()
    msg = driver.find_element(By.ID, "prompt").text
    print(msg)
    assert msg == f"Hello {input_val}! How are you today?"

    driver.find_element(By.ID, "promptbtn").click()
    time.sleep(2)
    alert.dismiss()
    cancel_msg = driver.find_element(By.ID, "prompt").text
    print(cancel_msg)
    assert  cancel_msg == "User cancelled the prompt."
    #assert  "cancelled" in cancel_msg
    #assert cancel_msg.istitle()

# handler_alert_box()
# handler_confirm_box()
handler_prompt_box()





