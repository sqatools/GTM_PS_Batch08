####### Number is Divisible by 3 ####

num = int(input("Enter a number: "))
var = int(input("Enter number with which you want to divide : "))
if num%var == 0:
	print(f"Number", {num} , " is divisible by : ", {num})
else:
	print(f"Number", {num} , " is divisible by :", {var})


###### If Number is even then find the Square and if number is odd then find it is Cube ########

num = int(input("Enter a number: "))
var = int(input("Enter number with which you want to divide ",{num}," : "))

if num%var == 0:
	print(f"Number", {num} , " is an even number")
	num1 = num * num
	print ("The square of " , {num} , " is: ", num1)
else:
	print(f"Number", {num} , " is an odd number")
	num1 = num * num * num
	print ("The Cube of " , {num} , " is: ", num1)


#######
