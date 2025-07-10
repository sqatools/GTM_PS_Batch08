import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.goibibo.com/")
driver.find_element(By.XPATH,"//span[@role='presentation']").click()
time.sleep(6)
driver.find_element(By.XPATH,"//a[@href='/bus/']//following-sibling::span[1]").click()
# window_list = driver.window_handles
# print(len(window_list))
# driver.switch_to.window(window_list[0])
time.sleep(5)
#from
from_source = driver.find_element(By.ID, "autosuggestBusSRPSrcHome")
from_source.send_keys("ISBT")

source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-1-item-0']//span")
source_dropdown_values.click()
time.sleep(5)
#to
to_source = driver.find_element(By.ID, "autosuggestBusSRPDestHome")
to_source.send_keys("HAMIRPUR")


to_source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-2-item-1']")
to_source_dropdown_values.click()
time.sleep(5)

travel_dat = driver.find_element(By.XPATH, "//span[contains(text(),'Tomorrow')]")
time.sleep(5)
travel_dat.click()
time.sleep(5)


tom_tab = driver.find_element(By.XPATH,"//button[@data-testid='searchBusBtn']")
tom_tab.click()
time.sleep(8)
