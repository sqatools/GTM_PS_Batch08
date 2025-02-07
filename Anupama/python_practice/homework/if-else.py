"""
print("*"*15,"check if given number is divisible by 3", "*"*15)
a = int(input("Integer value of a: "))
if (a%3)==0:
    print(a,"is divisible by 3")
else:
    print(a,"is not divisible by 3")
print("-"*50)

print("*"*15,"print square of even number and cube of odd number", "*"*15)
a = int(input("Integer value of a: "))
if(a%2)==00:
    print("square of", a,"is",a**2)
else:
    print("Cube of",a, "is", a**3)
print("-"*50)


print("*"*15,"check  if given number is positive or negative", "*"*15)
a = int(input("Integer value of a: "))
print("Given number is: ", a)
if a<0:
    print("The number is negative: ", a)
else:
    print("The number is positive: ", a)

print("-"*50)

print("*"*10,"check  if given number is divisible by 7 then add 50, else subtract 50 from number", "*"*10)
a = int(input("Integer value of a: "))
if(a%7)==0:
    print("Final value of",a ,"is: ",a+50)
else:
    print("Final value of",a,"is:", a-50)

print("-"*50)

print("*"*15,"simple calculator", "*"*15)
a = int(input("Integer value of a: "))
b = int(input("Integer value of b: "))
c = int(input("choose the operation 1 for '+' , 2 for '-', 3 for '*', 4 for '/' :"))
if c==1:
    print("The sum of a and b = ", a+b)
elif c==2:
    print("The difference of a and b = ", a - b)
elif c==3:
    print("The multiplied value of a and b = ", a * b)
elif c==4:
    print("A divided by b = ", a % b)
else:
    print("Invalid operation")
print("-"*50)

#**write a python code to simulate the interview process with the help nested if condition**

round1 = "fail"
round2 = "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats first round is cleared")

    if round2 == "pass":
        print("congrats second round is cleared")
        if round3 == "pass":
            print("congrats you are selected")
        else:
            print("Failed in last round, try next time")
    else:
        print("Failed in second round, try next time")

else:
    print("Failed in first round, try next time")
print("-"*50)

#**python program to find number of strings and numbers**
str1 = input("Enter your string: ")
letters = 0
digits = 0
for letter in str1:
    if letter.isalpha():
        letters += 1
    else:
        digits += 1
print(f"Letters {letters}")
print(f"Digits {digits}")
print("_"*100)

#***Python program to print the square or cube if the given number is divided by 2 or 3 respectively.")
num1=11
if num1%2==0:
    print("The square of",num1,"is",num1**2)
if num1%3==0:
    print("The cube of",num1,"is",num1**3)
if num1%2!=0 and num1%3!=0:
    print("The number is not divisible by 2 or 3 ")
print("_"*100)

#**Python program to find the largest number among three numbers.")
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))

if num1>num2 and num1>num3:
    print(num1,"is the greatest among",num1,num2,num3)
elif num2>num1 and num2>num3:
    print(num2,"is the greatest among",num1,num2,num3)
elif num3>num1 and num3>num2:
    print(num3,"is the greatest among",num1,num2,num3)
else:
    print("None of the numbers are greatest")
print("_"*100)

#**Python program to check any person eligible to vote or not")
print("age > 18+ : eligible")
print("age < 18: not eligible")

age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
print("_"*100)
"""



#**Ask the user for the name of the fruit and the weight in gms**
# Define the prices per gram for each fruit
fruit_prices = {
    "apple": .5,
    "banana": 0.99,
    "orange": .4,
    "pear": .40,}
fruit_name = input("Enter the name of the fruit: ")
fruit_weight = float(input("Enter the weight in gms: "))

# Calculate the total cost of the purchase
if fruit_name in fruit_prices:
    fruit_price = fruit_prices[fruit_name]
    total_cost = fruit_price * fruit_weight
    print(f"Total cost of {fruit_weight:.2f} grams of {fruit_name} is Rs.{total_cost:.2f}")
else:
    print(f"{fruit_name} is not available in the store")
print("_"*100)

#**program to show students average grade**
# Ask the user for the number of students
num_students = int(input("Enter the number of students: "))

# Initialize a variable to store the sum of grades
total_grade = 0

# Ask the user for the grades of each student and add it to the total grade
for i in range(num_students):
    grade = float(input(f"Enter the grade of student {i+1}: "))
    total_grade += grade

# Calculate the average grade
average_grade = total_grade / num_students

# Display the average grade to the user
print(f"The average grade of {num_students} students is {average_grade:.2f}")

# Ask the user for the symptoms of each patient and add them to the list**
# Initialize an empty list to store the symptoms
symptoms_list = []

# Ask the user for the symptoms of each patient and add them to the list
while True:
    symptoms = input("Enter the symptoms of the patient (or 'q' to quit): ")
    if symptoms == "q":
        break
    symptoms_list.append(symptoms)

symptoms_count = {} # Count the number of patients with each symptom
for symptom in symptoms_list:
    if symptom in symptoms_count:
        symptoms_count[symptom] += 1
    else:
        symptoms_count[symptom] = 1

# Display the number of patients with each symptom
for symptom, count in symptoms_count.items():
    print(f"{symptom}: {count}")
