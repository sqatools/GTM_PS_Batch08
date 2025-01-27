num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
decision=int(input("""Enter 1- For Addition 
Enter 2-For Subtraction 
Enter 3-For Multiplication 
Enter 4-For Division\n"""))

if decision==1:
    print(num1,"+",num2,"=", num1+num2)
elif decision==2:
    print(num1, "-", num2, "=", num1 - num2)
elif decision==3:
    print(num1,"*",num2,"=", num1*num2)
elif decision==4:
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("Invalid input")