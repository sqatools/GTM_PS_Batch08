from selenium import  webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://m.cricbuzz.com/profiles/265/dhoni")

table_element = driver.find_element(By.XPATH, "//h3[text()='Batting Career Summary']//following-sibling::div/table")

table_rows = table_element.find_elements(By.TAG_NAME, "tr")
print(len(table_rows))

for rows in table_rows:
    print(rows.text)
