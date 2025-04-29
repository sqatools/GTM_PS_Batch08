from selenium.webdriver.common.by import By


close_popup_icon = (By.XPATH, "//div[@data-id='auth-flow-section']//span[@role='presentation']")
bus_location_icon = (By.XPATH,"//a[@href='/bus/']")
source_city_input = (By.XPATH, "//div/label[text()='FROM']//following-sibling::input")
dest_city_input = (By.XPATH, "//div/label[text()='TO']//following-sibling::input")

