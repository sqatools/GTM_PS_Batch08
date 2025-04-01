 # //input[@aria-label="First name"]
 #      -> //input[@aria-label="Surname"]
 #      -> //select[@aria-label="Day"]
 #      -> //select[@aria-label="Month"]
 #      -> //select[@aria-label="Year"]

data_list= ['First name', 'Surname', 'Day', 'Month', 'Year']
for data in data_list:
    print(f"//select[@aria-label='{data}']")
