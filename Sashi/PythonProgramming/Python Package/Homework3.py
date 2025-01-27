
###WAP to create a calculator, Take 3 input where
#Number1 is input 1 and Number2 is input 2 and Descision for operation
#Descision 1 is for addition
#Descision 2 is for substraction
#Descision 3 is for multiplication
#Descision 4 is for division
#Descision 5 is for invalid descision value

num1 = int(input("Please Enter First Number:"))
num2 = int(input("Please Enter Second number:"))
descision = int(input("Please Enter Descision number:"))

if descision == 1:
    print("The Answer is:", num1+num2)
elif descision == 2:
    print("The Answer is:", num1-num2)
elif descision == 3:
    print("The Answer is:", num1*num2)
elif descision == 4:
    print("The Answer is:", num1/num2)
elif descision == 5:
    print("Invalid Descision Number")


""" when Descison value is 1
Please Enter First Number:10
Please Enter Second number:12
Please Enter Descision number:1
The Answer is: 22

### When Descision Value is 2
Please Enter First Number:20
Please Enter Second number:10
Please Enter Descision number:2
The Answer is: 10
###
Please Enter First Number:10
Please Enter Second number:20
Please Enter Descision number:3
The Answer is: 200
###
Please Enter First Number:20
Please Enter Second number:10
Please Enter Descision number:4
The Answer is: 2.0
###
Please Enter First Number:10
Please Enter Second number:20
Please Enter Descision number:5
Invalid Descision Number
"""