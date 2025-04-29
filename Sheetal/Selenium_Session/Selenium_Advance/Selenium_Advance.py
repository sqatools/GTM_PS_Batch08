import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

driver.find_element(By.LINK_TEXT, "What is Manual Testing").click()
driver.save_screenshot("main_window.png")

# window_handles, will return the list of widow tabs are available with their ID
windows_list = driver.window_handles
#driver.current_window_handle
print(windows_list)

time.sleep(2)
# switch to new tab
driver.switch_to.window(windows_list[1])

# take sacreenshot of new window
driver.save_screenshot("new_window.png")

# verify header on new window tab
header_elem = driver.find_element(By.XPATH, "//h3[@itemprop='name']")
print(header_elem.text)
assert header_elem.text == 'Manual Testing'

# click on API testing
driver.find_element(By.LINK_TEXT, "API Testing").click()

# close newly open tab
driver.close()
time.sleep(2)

# switch to main window
driver.switch_to.window(windows_list[0])
driver.save_screenshot("main_window2.png")

time.sleep(2)
driver.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

topics_list = ['Software Testing Principles',
               'Grey Box Testing',
               'White Box Testing',
               'Functional Testing']
count = 1
for topic in topics_list:
    driver.find_element(By.LINK_TEXT, topic).click()

    # window_handles, will return the list of widow tabs are available with their ID
    windows_list = driver.window_handles
    #driver.current_window_handle
    print(windows_list)

    time.sleep(2)
    # switch to new tab
    driver.switch_to.window(windows_list[1])

    # take sacreenshot of new window
    driver.save_screenshot(f"new_window_{count}.png")

    # verify header on new window tab
    header_elem = driver.find_element(By.XPATH, "//h3[@itemprop='name']")
    header_elem.screenshot(f"header_{count}.png")
    print(header_elem.text)

    driver.close()

    # switch to main window
    driver.switch_to.window(windows_list[0])
    driver.save_screenshot("main_window.png")
    count += 1

time.sleep(2)
driver.close()





import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

iframe_element = driver.find_element(By.XPATH, "//iframe[@name='globalSqa']")
driver.switch_to.frame(iframe_element)


mobile_menu = driver.find_element(By.ID, "mobile_menu_toggler")
mobile_menu.click()

time.sleep(5)
# mobile_menu_toggler

# switch to default content # move out of the iframe
driver.switch_to.default_content()

menu_tab = driver.find_element(By.XPATH, "//div[@id='menu']//a[@href='https://www.globalsqa.com/testers-hub/']")
menu_tab.click()
time.sleep(5)

time.sleep()














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


import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(15)



def perform_hover_operation():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    tab_menu_elem = driver.find_element(By.XPATH, "//div[@id='menu']//a[@href='https://www.globalsqa.com/testers-hub/']")

    action = ActionChains(driver)

    action.move_to_element(tab_menu_elem).perform()
    time.sleep(3)

    # hover to element demo site testing element, it will show other options
    demo_site_testing = driver.find_element(By.XPATH, "//span[text()='Demo Testing Site']//parent::a")
    action.move_to_element(demo_site_testing).perform()
    time.sleep(3)

    # hover to element and click on it.
    alert_box = driver.find_element(By.XPATH, "//span[text()='AlertBox']//parent::a")
    action.move_to_element(alert_box).click().perform()


#perform_hover_operation()

def perform_drag_and_drop_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    iframe_elem = driver.find_element(By.XPATH, "//iframe[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe_elem)

    image1_elem = driver.find_element(By.XPATH, "//h5[text()='High Tatras']//following-sibling::img")
    trash_elem = driver.find_element(By.ID, "trash")

    action = ActionChains(driver)
    #action.drag_and_drop(image1_elem, trash_elem).perform()
    action.drag_and_drop_by_offset(image1_elem, 200, 100)

    time.sleep(5)

    # Remaining images will be drag and dropped with the help of list of text.
    images_text = ['High Tatras 2', 'High Tatras 3', 'High Tatras 4']
    for img_text in images_text:
        image_elem = driver.find_element(By.XPATH, f"//h5[text()='{img_text}']//following-sibling::img")
        trash_elem = driver.find_element(By.ID, "trash")
        action.drag_and_drop(image_elem, trash_elem).perform()
        time.sleep(3)


#perform_drag_and_drop_operation()


import pyautogui
# pip install pyautogui

def perform_context_click_operation():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    about_menu_elem = driver.find_element(By.XPATH, "//div[@id='menu']//a[text()='About']")

    action = ActionChains(driver)
    action.context_click(about_menu_elem).perform()

    time.sleep(5)

    pyautogui.press("up")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(5)


#perform_context_click_operation()

def scroll_to_element_operation():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
    alert_box_elem = driver.find_element(By.XPATH, "//ul[@id='menu-miscellaneous-1']//a[text()='AlertBox']")

    action = ActionChains(driver)
    action.scroll_to_element(alert_box_elem).perform()

    time.sleep(5)

scroll_to_element_operation()


import time

from selenium import  webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://automationbysqatools.blogspot.com/2020/08/login.html")

upload_element = driver.find_element(By.ID, "myFile")
upload_element.send_keys(["E:\\Filesdata\\count_name.txt"])

time.sleep(5)

driver.find_element(By.XPATH, "(//input[@type='submit'])[1]").click()

time.sleep(5)
driver.close()





# Home work
# automate create facebook acount to pratice dropdown
