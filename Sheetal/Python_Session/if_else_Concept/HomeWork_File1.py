#1). write a python program to check given number is divisible by 3 or not
#2). write a python print square(n**2) if number is even or print cube(n**3) if number is odd
#3). write a python program to check given positive or negative.
#4).  Check given number is divisible by 7 then add 50 in the number else subtraction 50 from the


####### Number is Divisible by 3 ####

num = int(input("Enter a number: "))
var = int(input("Enter number with which you want to divide : "))
if num%var == 0:
	print(f"Number", {num} , " is divisible by : ", {var})
else:
	print(f"Number", {num} , " is not divisible by :", {var})


###### If Number is even then find the Square and if number is odd then find it is Cube ########

#num = int(input("Enter a number: "))
#var = int(input("Enter number with which you want to divide : "))

if num%var == 0:
	print(f"Number", {num} , " is an even number")
	num1 = num * num
	print ("The square of " , {num} , " is: ", num1)
else:
	print(f"Number", {num} , " is an odd number")
	num1 = num * num * num * num
	print ("The Cube of " , {num} , " is: ", num1)


####### Check given no. is +ve or -ve if +ve add 50 else sub 50 #######

#num = int(input("Enter a number: "))

if num > 0:
	print(f"Number", {num}, " is a positive number")

elif num < 0:
	print(f"Number", {num}, " is negative number")
else:
	print(f"Number", {num}, " is a zero number")

#num = int(input("Enter a number: "))
var = 7

if num%var == 0:
	num = num + 50
	print(f"The value of number is : ", {num})
else:
	num = num - 50
	print(f"The value of number is : ", {num})

