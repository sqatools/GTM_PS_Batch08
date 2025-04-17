from datetime import datetime, timedelta
import time

print("current datetime :", datetime.now()) # 2025-03-10 21:25:50.372012

print("current year :", datetime.now().year) # 2025
print("current date :", datetime.now().date()) # 2025-03-10
print("current month :", datetime.now().month) # 3
print("current day :", datetime.now().day) # 10
print("current time :", datetime.now().time()) # 21:27:35.021952

var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%h_%D")
"""
%m : month
%M : minutes
%Y : Year :" 2025
%y : Year : 25
%H : Hour
%S : Seconds
%h : month name : Mar
%D : date : 03/10/2025

"""
print(var)

def write_file(filename):
    with open(filename, "w") as file:
        file.write("Goog Morning")


# for i in range(5):
#     var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
#     filename = f"{var}.txt"
#     write_file(filename)
#     time.sleep(2)


"""
# get time difference between two activity
t1 = time.time()
time.sleep(5)
t2 = time.time()
print("time difference :", t2-t1)
"""

# time shows in epoc time format
print(time.time()) # 1741623558.8485603

# get yesterday date
yesterday = datetime.now() - timedelta(2)
print(yesterday)

print(datetime.strftime(yesterday, "%y-%m-%d")) # 25-03-08

# two house ago time.
two_hours_ago = datetime.now() - timedelta(hours=2)
print(two_hours_ago)
