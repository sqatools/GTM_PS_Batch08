# ########### 1. given number is divisible by 3 or not ###########

num=int(input("enter the number"))
if num %3==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")
#
# ############ 2. Print square if the no is even or print cube if the no is odd #######
#
num=int(input("enter the number"))
if num %2==0:
    print("Number is even")
    print("output is:", num**2)
else:
    print("Number is odd")
    print("output is:", num**3)

# ########### 3. given number is positive or negative ##########
#
num=int(input("enter the number"))
if num>=0:
    print("Number is positive")
else:
    print("Number is negative")

####### 4. given no divisible by 7 and add 50 , else subtract 50
num=int(input("enter the number"))
if num %7==0:
    print("Number is divisible by 7")
    print("output is:", num+50)
else:
    print("Number is not divisible by 7")
    print("output is:", num-50)

