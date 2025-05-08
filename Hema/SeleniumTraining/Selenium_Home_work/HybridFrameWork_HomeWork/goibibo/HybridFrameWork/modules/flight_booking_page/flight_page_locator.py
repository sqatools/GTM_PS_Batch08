from selenium.webdriver.common.by import By


close_popup_icon = (By.XPATH, "//div[@data-id='auth-flow-section']//span[@role='presentation']")
source_city_locator = (By.XPATH, "//span[text()='From']//following-sibling::p")
source_city_input = (By.XPATH, "//span[text()='From']//following-sibling::input")
dest_city_input = (By.XPATH, "//span[text()='To']//following-sibling::input")
