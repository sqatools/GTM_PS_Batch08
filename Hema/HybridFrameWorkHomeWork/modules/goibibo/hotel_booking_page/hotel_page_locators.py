from selenium.webdriver.common.by import By


close_popup_icon = (By.XPATH, "//span[@role='presentation']")
#where_to_locator = (By.XPATH, "//input[@id='downshift-6-input']")
where_to_locator = (By.XPATH, "//span[contains(text(),'Where')]//parent::div/p")
where_to_input = (By.XPATH, "//span[contains(text(),'Where')]//parent::div/input")
#checkin_locator = (By.XPATH, "//span[contains(text(),'Check-in')]//parent::div/span[1]")
checkin_locator = (By.XPATH, "//span[contains(text(),'Check-in')]//parent::div")
checkout_locator = (By.XPATH, "//span[contains(text(),'Check-out')]//parent::div")
guest_room_locator = (By.XPATH, "//span[contains(text(),'Guests & Rooms')]//parent::div")
rooms_locator = (By.XPATH, "//span[contains(text(),'Guests & Rooms')]//parent::div")
add_room_locator=(By.XPATH, "//h4[contains(text(), '1')]//parent::div//following-sibling::span")
guest_locator = (By.XPATH, "//span[contains(text(), 'Guests & Rooms')]")
done_button_locator = (By.XPATH, "//button[text()='Done']")
search_button_locator = (By.XPATH, "//a[text()='SEARCH']")