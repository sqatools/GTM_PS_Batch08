from selenium.webdriver.common.by import By

close_popup_icon = (By.XPATH, "//div[@data-id='auth-flow-section']//span[@role='presentation']")
close_popup_icon1 = (By.XPATH, "//div[@data-id='dweb_pip_id']/p")
#source_city_locator = (By.XPATH, "//input[@placeholder='From']")

source_city_locator = (By.XPATH, "//span[text()='From']//following-sibling::p")
dest_city_locator = (By.XPATH, "//span[text()='To']//following-sibling::p")
#source_city_input = (By.XPATH, "//span[text()='From']//following-sibling::input")
source_city_input = (By.XPATH, "//input[@placeholder='From']")
dest_city_input = (By.XPATH, "//input[@placeholder='To']")
#dest_city_input = (By.XPATH, "//span[text()='To']//following-sibling::input")
#departure_data_locator = (By.XPATH, "//span[text()='Departure']//parent::label")
departure_data_locator = (By.XPATH, "//div[@data-cy ='flightSW']")

# student website locator
username_field = (By.XPATH, "//input[@id='username']")
password_field = (By.XPATH, "//input[@id='password']")
submit_btn = (By.XPATH, "//button[@id='submit']")
success_msg_loc = (By.XPATH, "//h1[@class='post-title']")
travel_class_loc = (By.XPATH, "//span[text()='Travellers & Class']//ancestor::div[@data-cy = 'flightTraveller']")
flight_class_loc = (By.XPATH, "//li[text()='Premium Economy']")
Apply_btn_loc = (By.XPATH, "//button[text()='APPLY']")
search_btn_loc = (By.XPATH, "//a[text()='Search']")
#bus_booking
bus_btn_loc = (By.XPATH, "//span[text()='Bus']")
bus_source_loc = (By.XPATH, "//label[text()='FROM']//following::input[@placeholder='Enter Source']")
bus_dest_loc = (By.XPATH, "//label[text()='TO']//following::input[@placeholder='Enter Destination']")
bus_select_date = (By.XPATH, "//input[@placeholder='Pick a date']")
bus_search_btn = (By.XPATH, "//button[text()='Search Bus']")
