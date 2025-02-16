print('_'*50)
# Program to perform mathematical operations on two numbers.
"""
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operation = input("Enter operation of your choice: ")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "/":
    print(num1/num2)
elif operation == "*":
    print(num1*num2)
else:
    print("Invalid operation")

"""
print('_'*50)

# Accept marks from the user allot the stream based on marks
"""
marks = int(input("Enter Student Mark: "))

if 85 <= marks <101:
    print("Stream is: Science")
elif 70 <= marks < 85:
    print("Stream is: Commerce")
elif 35 <= marks < 70:
    print("Stream is: Arts")
elif 0 < marks < 35:
    print("Stream is: Fail")
else:
    print("Invalid marks")

"""
print('_'*50)
#Accept the temperature in Fahrenheit and check whether the water is boiling
"""
temp = int(input("Enter temperature of water in Fahrenheit: "))

if temp != 212:
    print("Water is not boiling")
else:
    print("Water is boiling")

"""
print('_'*50)
#Find the lowest number between three numbers.
"""
num1 = 100
num2 = 5
num3 = 200

if num1<num2:
    if num1<num3:
        print("Lowest no: ",num1)
elif num2<num1:
    if num2<num3:
        print("Lowest no: ",num2)
else:
    print("Lowest no: ",num3)
"""

print('_'*50)
# Check whether the given citizen is a senior citizen
"""
age = int(input("Enter your age : "))

if age >= 60:
    print("you are senior citizen")
else:
    print("you are not senior citizen")
    
"""
print('_'*50)
# Accept the city name and display its monuments
"""
city = input("Enter city name: ").lower()

if city == "pune":
    print("Shaniwar vada\nLal mahal\nSinhgad fort")
elif city == "mumbai":
    print("Getway of India\nGandhi statue\nAjanta cave")
else:
    print("Invalid city")

"""
print('_'*50)
# Take input from the user print the day according to the number.
"""
num = int(input("Enter a number: "))

if num == 1:
    print("Sunday")
elif num == 2:
    print("Monday")
elif num == 3:
    print("Tuesday")
elif num == 4:
    print("Wednesday")
elif num == 5:
    print("Thursday")
elif num == 6:
    print("Friday")
elif num == 7:
    print("Saturday")
else:
    print("Invalid number")

"""
print('_'*50)
# Accept the car price and display the road tax to be paid
"""
amount = int(input("Enter car price: "))

if amount <= 500000:
     print("Tax payable: ",15000)
elif 500000 < amount <= 1000000:
     print("Tax payable: ",50000)
else:
    print("Tax payable: ",80000)

"""
print('_'*50)
#Program to display 1/0 if the user gives Hello/Bye as output.
"""
input = input("Enter your choice: ")

if input == "Hello":
    print(1)
elif input == "Bye":
    print(0)
else:
    print("Invalid choice")
    
"""

print('_'*50)
#Check whether the last digit of a number is divisible by 4

num = 200
last_digit = num%10

if last_digit%4 == 0:
    print("The last digit is divisible by 4")
else:
    print("The last digit is not divisible by 4")