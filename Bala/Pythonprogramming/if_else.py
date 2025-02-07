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

####### 5. Pattern printing #############
for i in range(6):
    print(i*"*")
for i in range(4,-1,-1):
    print(i*"*")

###### 6. printing the given numbers##########
# for i in range(0,11):
#     if i !=3 or i !=6
#         print(i,end=" ")

######## 7. printing the text in between numbers#########
for i in range(3,9):
    if (i==3) or (i==5):
        print("hello")
    print(i)
######### example 8 ###########
for i in range(0,11):
        if i != 3 or i != 6:
            print(i,end=" ")

######### example ######
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

######


