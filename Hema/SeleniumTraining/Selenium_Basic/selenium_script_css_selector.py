"""
# Type of CSS Selector in selenium
1. ID.   with css selector we can mention id with # symbol to indentify it.
        faceboo.com
      -> #email
      -> #pass
2. Class. :  class css selected define with dot as prefix for each of the class of the element.
      -> ._42ft._4jy0._6lth._4jy6._4jy1.selected._51sy
      -> .post-title

3. Attribute. :  Attribute css selector use the any of the attribute of the element
            e.g.  tagname[attribute='value']
            -> button[data-testid='royal-login-button']
            -> input[data-testid='royal-email']
            -> input[data-testid='royal-pass']

4. sub-string. : with the help sub-string method, we can use partial value of attributes to write
                 the css selector
                 # attribute^ for start prefix value and attribute*
                 # Matching a substring starts-with^
                 e.g. tagname[attribute^='value']
                 -> input[data-testid^='royal-e']
                 -> input[data-testid^='royal-p']

                 # Matching a substring (contains:*)
                 e.g. tagname[attribute*='value']
                 -> input[data-testid*='l-pass']
                 -> input[data-testid*='l-email']
                 -> button[data-testid*='login']

                 # Matching a substring with end value (contains:$)
                 e.g. tagname[attribute$='end-value']
                 -> button[data-testid$='login-button']
                 -> input[data-testid$='l-pass']
                 -> [data-testid$='form-button']


5. parent-child-path :
                  -> form>div>a[data-testid="open-registration-form-button"]
                  -> div>button[data-testid="royal-login-button"]
                  -> div[align="left"]>ul
                  -> div>div[align="left"]>ul


"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initiate a webdriver
driver = webdriver.Chrome()
# maximize browser window
driver.maximize_window()
# set implicit wait
driver.implicitly_wait(10)

def facebook_website():
    # launch website URL on browser.
    driver.get("https://www.facebook.com")

    # select by ID css selector
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("user1@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("user@1234")

    # ._42ft._4jy0._6lth._4jy6._4jy1.selected._51sy # CSS SELECTOR
    time.sleep(5)
    #driver.find_element(By.CSS_SELECTOR, "._42ft._4jy0._6lth._4jy6._4jy1.selected._51sy").click()

    # # _42ft _4jy0 _52e0 _4jy6 _4jy1 selected _51sy # CLASS SELECTOR
    #driver.find_element(By.CLASS_NAME, "_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy").click()

    # Attribute CSS Selector
    driver.find_element(By.CSS_SELECTOR, "button[data-testid='royal-login-button']").click()



def dummy_website():
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

    #CLASS NAME
    # header = driver.find_element(By.CLASS_NAME, "post-title")
    #print(header.text)

    #CSS_SELECTOR
    # header = driver.find_element(By.CSS_SELECTOR, ".post-title")
    # print(header.text)

    # TAGNAME
    header_name = driver.find_element(By.TAG_NAME, "h1").text
    print(header_name)


#facebook_website()
dummy_website()

time.sleep(10)
driver.close()



