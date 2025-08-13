from selenium.webdriver.common.by import By

close_popup_icon = (By.XPATH, "//div[@data-id='auth-flow-section']//span[@role='presentation']")
source_city_locator = (By.XPATH, "//span[text()='From']//following-sibling::p")
source_city_input = (By.XPATH, "//span[text()='From']//following-sibling::input")
dest_city_input = (By.XPATH, "//span[text()='To']//following-sibling::input")
departure_data_locator =(By.XPATH, "//span[text()='Departure']//parent::div")

# student website locator
username_field = (By.XPATH, "//input[@id='username']")
password_field = (By.XPATH, "//input[@id='password']")
submit_btn = (By.XPATH, "//button[@id='submit']")
success_msg_loc =(By.XPATH,"//h1[@class='post-title']")

