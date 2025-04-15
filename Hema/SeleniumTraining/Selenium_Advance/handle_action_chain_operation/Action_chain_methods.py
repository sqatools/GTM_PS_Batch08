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


