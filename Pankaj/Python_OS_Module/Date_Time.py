from datetime import datetime
import time

print("Current date time: ", datetime.now())

print("Current year: ", datetime.now().year)
print("Current Date: ", datetime.now().date())
print("Current Time: ", datetime.now().time())

var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
print(var)


def write_file(filename):
    with open(filename, "w") as file:
        file.write("Good Morning")


for i in range(5):
    var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    filename = f"{var}.txt"
    write_file(filename)
    time.sleep(2)
