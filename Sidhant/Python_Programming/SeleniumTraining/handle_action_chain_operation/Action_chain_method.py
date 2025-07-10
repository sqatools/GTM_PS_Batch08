import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait( 10 )


def hover_method():
    driver.get( "https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame" )
    tab_menu = driver.find_element( By.XPATH, "//div[@id ='menu']//a[@href='https://www.globalsqa.com/testers-hub/']" )
    action = ActionChains( driver )
    action.move_to_element( tab_menu ).perform()
    time.sleep( 5 )
    demo_site = driver.find_element( By.XPATH, "//span[text()='Demo Testing Site']//parent::a" )
    action.move_to_element( demo_site ).perform()
    time.sleep( 3 )
    alert_box = driver.find_element( By.XPATH, "//span[text()='AlertBox']//parent::a" )
    action.move_to_element( alert_box ).click().perform()
    time.sleep( 3 )
    window_list = driver.window_handles
    driver.switch_to.window( window_list[0] )
    time.sleep( 9 )


# hover_method()

# perform drag and drop
def drag_and_drop_operation():  #Putting image in trash
    driver.get( "https://www.globalsqa.com/demo-site/draganddrop/" )
    iframe_elem = driver.find_element(By.XPATH,"//iframe[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe_elem)
    images_text = ['Planning the ascent', 'On top of Kozi kopka','The chalet at the Green mountain lake']
    for img in images_text:
        image1_elm = driver.find_element( By.XPATH, f"//img[@alt='{img}']" )
        trash_box = driver.find_element( By.XPATH, "//div[@id='trash']" )
        action = ActionChains( driver )
        action.drag_and_drop( image1_elm, trash_box ).perform()
        time.sleep( 5 )

#drag_and_drop_operation()
import pyautogui
def perform_context_click_operation():
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    about_menu_elem = driver.find_element(By.XPATH,"//a[text()='About']")
    action = ActionChains(driver)
    action.context_click(about_menu_elem).perform()               #context_click means right click
    time.sleep(4)
    pyautogui.press( "up" )
    time.sleep( 4 )
    pyautogui.press( "enter" )
    time.sleep( 4 )

#perform_context_click_operation()

def scroll_to_element_operation():
    driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame" )
    tool_elem = driver.find_element(By.XPATH,"//ul[@id='menu-miscellaneous-1']//a[text()='AlertBox']")
    action = ActionChains(driver)
    action.scroll_to_element(tool_elem).perform()
    time.sleep(5)
scroll_to_element_operation()