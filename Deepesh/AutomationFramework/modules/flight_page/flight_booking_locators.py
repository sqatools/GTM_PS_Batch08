from selenium.webdriver.common.by import By

close_popup_loc = (By.XPATH, "//span[@class='logSprite icClose']")
source_city_label = (By.XPATH, "//span[text()='From']//following-sibling::p")
source_city_field = (By.XPATH, "//span[text()='From']//following-sibling::input")
dest_city_field = (By.XPATH, "//span[text()='To']//following-sibling::input")
depart_date_label = (By.XPATH, "//span[text()='Departure']//parent::div")
depart_date_value = (By.XPATH, "//div[contains(@aria-label,'Jun 20 2025')]")

