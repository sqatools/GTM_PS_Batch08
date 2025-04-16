'''
goibibo

URL:
https://www.goibibo.com/flights/?utm_source=bing&utm_medium=cpc&utm_campaign=DF-Brand-EM&utm_adgroup=Only%20Goibibo&utm_term=!SEM!DF!B!Brand!RSA!150035352!1211662109442708!!e!goibibo!c!

'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
alert = Alert(driver)
def launch_url():

    driver.get("https://www.goibibo.com/")
    close_icon = driver.find_element(By.XPATH, "//span[@role='presentation']")
    close_icon.click()
    time.sleep(5)

def notification_prompt():
    onsite_iframe_element = driver.find_element(By.ID, "webpush-onsite")
    driver.switch_to.frame(onsite_iframe_element)

    onsite_push_cancel = driver.find_element(By.XPATH, "//div[@class='button-group-custom clearfix']/button[1]")
    onsite_push_allow = driver.find_element(By.XPATH, "//div[@class='button-group-custom clearfix']/button[2]")

    onsite_push_cancel.click()
    time.sleep(5)

def header_items():
    driver.switch_to.default_content()

    main_header_items = driver.find_elements(By.XPATH, "//header[@data-id='dweb-header-root']//li/a/span[2]")
    print(len(main_header_items))

    for header_item in main_header_items:
        print(header_item.text, end=" ")
        # time.sleep(2)
        #
        # if header_item.text == "Bus":
        #     bus_link = driver.find_element(By.XPATH, "//a[@href='/bus/']/span[1]")
        #     bus_link.click()
        # else:
        #     print("hello")

    time.sleep(5)

def bus_item_with_tomorrow_option():

    list_bus_names = []
    location_detail_list =[]
    bus_link = driver.find_element(By.XPATH, "//a[@href='/bus/']/span[1]")
    bus_link.click()

    # From_bus_option
    from_source = driver.find_element(By.ID, "autosuggestBusSRPSrcHome")
    from_source.send_keys("Chennai")

    source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-1-item-1']//span")
    source_dropdown_values.click()

    time.sleep(10)

    #To_bus_option
    to_source = driver.find_element(By.ID, "autosuggestBusSRPDestHome")
    to_source.send_keys("Bangalore")
    time.sleep(2)

    to_source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-2-item-4']//span")
    to_source_dropdown_values.click()
    time.sleep(5)

    #Travel date 'Tommorrow' option

    travel_dat = driver.find_element(By.XPATH, "//span[contains(text(),'Tomorrow')]")
    time.sleep(5)
    travel_dat.click()
    time.sleep(5)

    #Search_button_option
    search_button=driver.find_element(By.XPATH, "//button[@data-testid='searchBusBtn']")
    search_button.click()
    time.sleep(5)

    #to get the total number of bus names
    bus_names = driver.find_elements(By.XPATH, "//div[@class='SrpActiveCardstyles__LayoutFirstDiv-sc-yk1110-4 ijRmXM']/p[1]")
    print("The length of the bus names: \n", len(bus_names))


    #xpath:
    #dropping_point: //p[text()='Dropping Point']//following-sibling::div//p[text()='ATTIBELLI']//parent::div//preceding-sibling::label
    #boarding_point: //p[text()='Dropping Point']//following-sibling::div//p[text()='ATTIBELLI']//parent::div//preceding-sibling::label

    #printing the bus names
    for bus_name in bus_names:
        #print("\n",bus_name.text)
        list_bus_names.append(bus_name.text)

    print("The list of bus names are: \n", list_bus_names)

    total_seats = driver.find_elements(By.XPATH, "//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
    print("The length of the total seats are: \n", len(total_seats))

    # for seat in total_seats:
    #     print(seat.text, end="\n")

    #based on the bus name clicking seat option

    select_bus_name = 'CIT TRAVELS'

    if select_bus_name in list_bus_names:
        select_seat_option = driver.find_element(By.XPATH, "//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
        select_seat_option.click()

    # point_headers = driver.find_element(By.XPATH, "//p[@class='boxHeaders']")
    # print(point_headers.text)

    # radio_buttons = driver.find_elements(By.XPATH, "//span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl']")
    # print("The length of the radio buttons: ", len(radio_buttons))

    location_details = driver.find_elements(By.XPATH, "//p[@class='location']")
    print("The length of the location details: ", len(location_details))

    #to get the location details

    for location_detail in location_details:
        #print("\n", location_detail.text)
        location_detail_list.append(location_detail.text)
    print("The list of location details are: \n", location_detail_list)

    location_detail = driver.find_element(By.XPATH, "//p[@class='location']")
    radio_button = driver.find_element(By.XPATH, "//span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl']")

    boarding_point = driver.find_element(By.XPATH, "//p[text()='Boarding Point']//following-sibling::div//p[text()='Tharamani']//parent::div//preceding-sibling::label")
    boarding_point.click()

    time.sleep(5)

    #facing issue in dropping point - Fixed it by increasing time.sleep
    #dropping_point = driver.find_element(By.XPATH, "//p[text()='Dropping Point']//following-sibling::div//p[text()='Electronic City']//parent::div//preceding-sibling::label")
    #dropping_point = driver.find_element(By.XPATH, "//p[text()='Dropping Point']//following-sibling::div//p[text()='Bommasandra']//parent::div//preceding-sibling::label")
    dropping_point = driver.find_element(By.XPATH, "//p[contains(text(),'Dropping Point')]//following-sibling::div//p[text()='Bommasandra']//parent::div//preceding-sibling::label")
    dropping_point.click()

    time.sleep(5)

    seat_fill = driver.find_element(By.XPATH, "//div[@class='SeatWithTooltipstyles__BusSeat-sc-dkrka-2 kBvUB']")
    seat_fill.click()

    time.sleep(2)
    continue_button = driver.find_element(By.XPATH, "//button[@class='SelectSeatTabContentstyles__Button-sc-aw7o7o-9 cZetwz']")
    continue_button.click()

    time.sleep(15)

    boarding_point_details = driver.find_elements(By.XPATH, "//p[text()='Tharamani']/parent::section/p")
    for boarding_detail in boarding_point_details:
        print("\n", boarding_detail.text)

    time.sleep(15)

    dropping_point_details = driver.find_elements(By.XPATH, "//p[contains(text(),'Bommasandra')]/parent::section/p")
    for dropping_detail in dropping_point_details:
        print("\n", dropping_detail.text)

    time.sleep(15)

    price_details = driver.find_elements(By.XPATH, "//span[text()='Total Basefare']/ancestor::section/div")
    for price_detail in price_details:
        print("Price details are: \n", price_detail.text)

    time.sleep(15)

def bus_item_with_today_option():

    list_bus_names = []
    location_detail_list =[]
    bus_link = driver.find_element(By.XPATH, "//a[@href='/bus/']/span[1]")
    bus_link.click()

    # From_bus_option
    from_source = driver.find_element(By.ID, "autosuggestBusSRPSrcHome")
    from_source.send_keys("Chennai")

    source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-1-item-1']//span")
    source_dropdown_values.click()

    time.sleep(10)

    #To_bus_option
    to_source = driver.find_element(By.ID, "autosuggestBusSRPDestHome")
    to_source.send_keys("Bangalore")
    time.sleep(2)

    to_source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-2-item-4']//span")
    to_source_dropdown_values.click()
    time.sleep(5)

    #travel date with today option
    today_date_check =driver.find_element(By.XPATH, "//input[@placeholder='Pick a date']")
    print(today_date_check.text)

    time.sleep(5)

    date_option = driver.find_element(By.XPATH, "//span[@class='active']")
    date_value_text = date_option.text
    print(date_value_text)
    time.sleep(5)

    #date_option.click()

    # Search_button_option
    search_button = driver.find_element(By.XPATH, "//button[@data-testid='searchBusBtn']")
    search_button.click()
    time.sleep(5)


    update_date = driver.find_element(By.XPATH, "//input[@data-testid='openCheckinCalendar']")
    update_date.click()

    time.sleep(5)

    date_value_list = []
    #totaldate in a month
    #date_values = driver.find_elements(By.XPATH, "//li[@style='color: black;']//ancestor::div/ul[2]/li")

    date_values = driver.find_elements(By.XPATH, "//li[@style='color: black;']")

    for date_value in date_values:
        #print(date_value.text)
        date_value_list.append(date_value.text)
        #time.sleep(5)

    list_date_value = date_value_text.split(" ")
    extract_date = ''

    print(list_date_value)
    for i in range(len(list_date_value)):
        if i == 2:
            extract_date = extract_date + list_date_value[i]
            break
        else:
            continue

    print("Date: ", extract_date)

    time.sleep(15)
    print(date_value_list)

    if extract_date in date_value_list:
        click_date = driver.find_element(By.XPATH,"//span[text()='16']")
        click_date.click()
    time.sleep(15)

    update_search = driver.find_element(By.XPATH, "//span[@data-testid='searchBusBtnSRP']")
    update_search.click()
    time.sleep(15)

    #to get the total number of bus names
    bus_names = driver.find_elements(By.XPATH, "//p[@class='SrpActiveCardstyles__BusBoldtxtPara-sc-yk1110-7 faoGPx']//parent::div/p")
    print("The length of the bus names: \n", len(bus_names))


    #xpath:
    #dropping_point: //p[text()='Dropping Point']//following-sibling::div//p[text()='ATTIBELLI']//parent::div//preceding-sibling::label
    #boarding_point: //p[text()='Dropping Point']//following-sibling::div//p[text()='ATTIBELLI']//parent::div//preceding-sibling::label

    #printing the bus names
    for bus_name in bus_names:
        #print("\n",bus_name.text)
        list_bus_names.append(bus_name.text)

    print("The list of bus names are: \n", list_bus_names)

    total_seats = driver.find_elements(By.XPATH, "//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
    print("The length of the total seats are: \n", len(total_seats))

    # for seat in total_seats:
    #     print(seat.text, end="\n")

    #based on the bus name clicking seat option

    select_bus_name = 'KBS Luxury Bus'

    if select_bus_name in list_bus_names:
        select_seat_option = driver.find_element(By.XPATH, "//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
        select_seat_option.click()
    else:
        print("bus name is not available, hence unable to select seat")


    location_details = driver.find_elements(By.XPATH, "//p[@class='location']")
    print("The length of the location details: ", len(location_details))

    #to get the location details

    for location_detail in location_details:
        #print("\n", location_detail.text)
        location_detail_list.append(location_detail.text)
    print("The list of location details are: \n", location_detail_list)

    location_detail = driver.find_element(By.XPATH, "//p[@class='location']")


    boarding_point = driver.find_element(By.XPATH, "//p[text()='Boarding Point']//following-sibling::div//p[text()='Tharamani']//parent::div//preceding-sibling::label")
    boarding_point.click()

    time.sleep(5)

    #facing issue in dropping point - Fixed it by increasing time.sleep
    #dropping_point = driver.find_element(By.XPATH, "//p[text()='Dropping Point']//following-sibling::div//p[text()='Electronic City']//parent::div//preceding-sibling::label")
    #dropping_point = driver.find_element(By.XPATH, "//p[text()='Dropping Point']//following-sibling::div//p[text()='Bommasandra']//parent::div//preceding-sibling::label")
    dropping_point = driver.find_element(By.XPATH, "//p[contains(text(),'Dropping Point')]//following-sibling::div//p[text()='Bommasandra']//parent::div//preceding-sibling::label")
    dropping_point.click()

    time.sleep(5)

    seat_fill = driver.find_element(By.XPATH, "//div[@class='SeatWithTooltipstyles__BusSeat-sc-dkrka-2 kBvUB']")
    seat_fill.click()

    time.sleep(2)
    continue_button = driver.find_element(By.XPATH, "//button[@class='SelectSeatTabContentstyles__Button-sc-aw7o7o-9 cZetwz']")
    continue_button.click()

    time.sleep(15)

    boarding_point_details = driver.find_elements(By.XPATH, "//p[text()='Tharamani']/parent::section/p")
    for boarding_detail in boarding_point_details:
        print("\n", boarding_detail.text)

    time.sleep(15)

    dropping_point_details = driver.find_elements(By.XPATH, "//p[contains(text(),'Bommasandra')]/parent::section/p")
    for dropping_detail in dropping_point_details:
        print("\n", dropping_detail.text)

    time.sleep(15)

    price_details = driver.find_elements(By.XPATH, "//span[text()='Total Basefare']/ancestor::section/div")
    for price_detail in price_details:
        print("Price details are: \n", price_detail.text)

    time.sleep(15)

# def bus_header_item():
#
#     list_bus_names = []
#     location_detail_list =[]
#     bus_link = driver.find_element(By.XPATH, "//a[@href='/bus/']/span[1]")
#     bus_link.click()
#     from_source = driver.find_element(By.ID, "autosuggestBusSRPSrcHome")
#     from_source.send_keys("Chennai")
#
#     action = ActionChains(driver)
#
#     source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-1-item-1']//span")
#     #print(len(source_dropdown_values))
#     # for source_dropdown_value in source_dropdown_values:
#     #     print(source_dropdown_value, end=" ")
#     #source_dropdown_values.click()
#     source_dropdown_values.click()
#
#     time.sleep(10)
#     # source_click.click()
#     # #print(source_click.text)
#     to_source = driver.find_element(By.ID, "autosuggestBusSRPDestHome")
#     to_source.send_keys("Bangalore")
#     time.sleep(2)
#
#     to_source_dropdown_values = driver.find_element(By.XPATH, "//div[@id='downshift-2-item-4']//span")
#     #action.move_to_element(to_source_dropdown_values).click()
#     to_source_dropdown_values.click()
#     time.sleep(5)
#     #travel_dat = driver.find_element(By.XPATH, "//div[@class='SearchWidgetstyles__DateTabs-sc-1mr4hwz-4 gKiMdw']/span[@class='active']")
#     travel_dat = driver.find_element(By.XPATH, "//span[contains(text(),'Tomorrow')]")
#     time.sleep(5)
#     travel_dat.click()
#     time.sleep(5)
#     search_button=driver.find_element(By.XPATH, "//button[@data-testid='searchBusBtn']")
#     search_button.click()
#     time.sleep(5)
#
#     #bus_type=driver.find_element(By.XPATH, "//div[contains(text(),'AC')]")
#     bus_names = driver.find_elements(By.XPATH, "//div[@class='SrpActiveCardstyles__LayoutFirstDiv-sc-yk1110-4 ijRmXM']/p[1]")
#     print("\n", len(bus_names))
#
#
#     #xpath:
#     #dropping_point: //p[text()='Dropping Point']//following-sibling::div//p[text()='ATTIBELLI']//parent::div//preceding-sibling::label
#     #boarding_point: //p[text()='Dropping Point']//following-sibling::div//p[text()='ATTIBELLI']//parent::div//preceding-sibling::label
#
#     for bus_name in bus_names:
#         #print("\n",bus_name.text)
#         list_bus_names.append(bus_name.text)
#
#     print(list_bus_names)
#
#     total_seats = driver.find_elements(By.XPATH, "//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
#     print("\n", len(total_seats))
#
#     # for seat in total_seats:
#     #     print(seat.text, end="\n")
#
#     select_bus_name = 'CIT TRAVELS'
#
#     if select_bus_name in list_bus_names:
#         select_seat_option = driver.find_element(By.XPATH, "//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
#         select_seat_option.click()
#
#     point_headers = driver.find_element(By.XPATH, "//p[@class='boxHeaders']")
#     print(point_headers.text)
#
#     radio_buttons = driver.find_elements(By.XPATH, "//span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl']")
#     print(len(radio_buttons))
#
#     location_details = driver.find_elements(By.XPATH, "//p[@class='location']")
#     print(len(location_details))
#
#     for location_detail in location_details:
#         #print("\n", location_detail.text)
#         location_detail_list.append(location_detail.text)
#     print(location_detail_list)
#
#     location_detail = driver.find_element(By.XPATH, "//p[@class='location']")
#     radio_button = driver.find_element(By.XPATH, "//span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl']")
#
#     if point_headers.text == 'Boarding Point':
#         print("Boarding point")
#         location_detail = driver.find_element(By.XPATH, "//p[@class='location']")
#         if location_detail.text == 'Koyembedu':
#             radio_button = driver.find_element(By.XPATH, "//span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl']")
#             print(radio_button.is_selected())
#             radio_button.click()
#             print(radio_button.is_selected())
#     #dropping_point = driver.find_element(By.XPATH, "//p[@class='boxHeaders']")
#
#     if point_headers.text == 'Dropping Point':
#         location_detail = driver.find_element(By.XPATH, "//p[@class='location']")
#         if location_detail.text == 'Electronicity':
#             radio_button = driver.find_element(By.XPATH,"//span[@class='RadioButtonstyles__Checkmark-sc-wz601o-1 bFGqGl']")
#             print(radio_button.is_selected())
#             radio_button.click()
#             print(radio_button.is_selected())
#
#     #//div[@class="BusBerthstyles__BusOutline-sc-rfhcvl-0 bDTuH"]/aside[2]
#     seat_fill = driver.find_element(By.XPATH, "//div[@class='SeatWithTooltipstyles__BusSeat-sc-dkrka-2 kBvUB']")
#     seat_fill.click()
#
#     continue_button = driver.find_element(By.XPATH, "//button[@class='SelectSeatTabContentstyles__Button-sc-aw7o7o-9 cZetwz']")
#     continue_button.click()
#
#     time.sleep(15)

def display():
    launch_url()
    notification_prompt()
    header_items()
    #NOT WORKING: #bus_header_item()
    #WORKING: bus_item_with_tomorrow_option()
    bus_item_with_today_option()

display()
driver.close()

