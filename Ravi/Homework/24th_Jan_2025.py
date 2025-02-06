num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))
decision_dict = {"1": "Addition", "2": "Subtraction", "3": "Multiplication", "4": "Division"}

decision = input("Please enter your mathematical decision by providing the number form the from the following choices"
                 "\n1. Add\n2. Subtract\n3. Multiplication\n4. Division\nYour choice:")
print("-"*40)
if decision == "1":
    print(decision_dict[decision]+" Result:"+str(num1+num2))
elif decision == "2":
    print(decision_dict[decision]+" Result:"+str(num1-num2))
elif decision == "3":
    print(decision_dict[decision]+" Result:"+str(num1*num2))
elif decision == "4":
    print(decision_dict[decision]+" Result:"+str(num1/num2))
else:
    print("Invalid decision selected")

print("-" * 40)
