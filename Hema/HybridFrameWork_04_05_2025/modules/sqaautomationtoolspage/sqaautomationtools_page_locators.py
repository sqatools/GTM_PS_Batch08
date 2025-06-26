from selenium.webdriver.common.by import By

title_text_locator = (By.XPATH, "//h1[contains(text(),' Dummy Ticket Booking Website')]")
option_return_tkt_locator = (By.XPATH, "//span[contains(text(),'Dummy return ticket')]")
option_tkt_visa_locator=(By.XPATH, "//span[contains(text(),'Dummy ticket for visa')]")
option_tkt_hotel_book_locator=(By.XPATH, "//span[contains(text(),'Dummy hotel booking')]")
option_tkt_hotel_flight_book_locator=(By.XPATH, "//span[contains(text(),'Dummy hotel  and flight')]")
option_cab_book_locator = (By.XPATH, "//span[contains(text(),'Cab booking and return')]")


first_name_input_locator = (By.XPATH, "//span[text()='    First Name    ']//parent::div//following::input[1]")
last_name_input_locator = (By.XPATH, "//span[text()='    Last Name     ']//parent::div//following::input[2]")

dob_locator = (By.XPATH, "//input[@id='birthday']")
female_locator = (By.XPATH, "//span[text()='Female']//parent::div//following-sibling::input[2]")
male_locator = (By.XPATH, "//input[@id='male']")
one_way_locator = (By.XPATH, "//input[@id='oneway']")


from_city_locator=(By.XPATH, "//input[@id='fromcity']")
dest_city=(By.XPATH, "//input[@id='destcity']")

depart_date=(By.XPATH, "//input[@id='departdate']")
return_date=(By.XPATH, "//input[@id='returndate']")
visa_date = (By.XPATH, "//input[@id='visadate']")

email_locator=(By.XPATH, "//input[@id='eamil']")
whatsapp_lcator=(By.XPATH, "//input[@id='whatsapp']")
both_locator = (By.XPATH, "//input[@id='whatsapp']//following::input[1]")

billing_name=(By.XPATH, "//input[@id='billing_name']")
billing_phone=(By.XPATH, "//input[@id='billing_phone']")
billing_email = (By.XPATH, "//input[@id='billing_email']")
billing_street=(By.XPATH, "//input[@id='billing_address']")

country_dropdown=(By.XPATH, "//select[@id='billing_country']")
postal=(By.XPATH, "//input[@id='postcode']")

street_address_1=(By.XPATH, "//input[@id='street_address1']")

city_checkbox=(By.XPATH, "//td[contains(text(),'6002')]//parent::tr/td/input")
