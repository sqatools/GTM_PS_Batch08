# write a python program to check greater number among three values

"""
a = int(input("Please enter value of a :"))
b = int(input("Please enter value of b :"))
c = int(input("Please enter value of c :"))


if a > b and a > c:
    print("A is greatest among all,", a)
elif b > c and b > a:
    print("B is greatest among all,", b)
elif c > a and c > a:
    print ("C is the greatest among all,",c)
"""



"""
# write a python program to provide the grade to the students as per the marks obtained.


marks = int(input("please enter your marks:"))

if marks >= 35 and marks < 50:
    print(" Congratulations you have passed the exam with grade C")
elif marks >= 50 and marks < 75:
    print("Congratulations you have passed the exam with grade B")
elif marks >= 75 and marks < 90:
    print(" Congratulations you have passed the exam with grade A")
elif marks >= 90 and marks <= 100:
    print(" Congratulations you have passed the exam with grade A+")
elif marks < 35:
    print("Better luck next time")


"""

# Home : Write a python program to create a calculator
"""
Take three input user, num1, num2, decision
if decision ==1 : add num1, num2
if decision ==2 : sub num1, num2
if decision ==3 : multi num1, num2
if decision ==4 : division num1, num2
if decision > 4 : invalid input
"""
print("_____CALCULATOR_____")

number1=float(input("please enter First Number1:"))
number2=float(input("please enter First Number2:"))
decision = int(input("Please enter your choice 1: Add, 2: Subtract, 3: Multiply, 4: Divide " ))

if decision == 1:
  # Add =int (number1+number2)
    print("The result of Addition is:", number1 + number2)
elif decision == 2:
  #  Sub == number1 - number2
    print("The result of Substraction is:", number1 - number2)
elif decision == 3:
   # Multi == number1 * number2
    print("The result of Multiplication is:", number1 * number2)
elif decision == 4:
 #   Div == number1/number2
    print("The result of Addition is:", number1/number2)
else:
    print("Invalid input! Please enter a choice between 1 to 4.")

"""
Output:
please enter First Number1:34
please enter First Number2:3
Please enter your choice 1: Add, 2: Subtract, 3: Multiply, 4: Divide 3
The result of Multiplication is: 102.0


"""



