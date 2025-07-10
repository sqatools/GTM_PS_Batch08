import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.cricbuzz.com/cricket-series/9237/indian-premier-league-2025/points-table")
cric_table = driver.find_element(By.XPATH,"//h3[text()='IPL 2025 - Points Table']//parent::div")
table_row = cric_table.find_elements(By.TAG_NAME,"tr")
print(len(table_row))

for rows in table_row:
    print(rows.text)