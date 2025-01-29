#1)Python program to check given number is divided by 3 or not.
n=2
if n%3==0:
    print("the given number is divisible by 3")
else:
    print("the given number is not divisible by 3")
print ("_"*50)


#2)If else program to get all the numbers divided by 3 from 1 to 30.
for i in(1,30,1):
    if i%3==0:
        print (i)
print ("_"*50)

#3)else program to assign grades as per total marks.
marks=int(input("Enter the value:"))
a,b,c,d,e=0,35,60,85,100

if 0 > marks < 35:
    print("the grade is C")
elif 35 > marks and marks < 60:   # 35>10<60
    print("the grade is B")
elif  60 > marks and marks < 85:
    print("the grade is A")
elif  100 > marks<0:
    print("the grade is Fail")
else:
    print("the grade is invalid")
print("_"*50)

# 4) Python program to check the given number divided by 3 and 5.
a=int((input("Enter the number:")))
if a%3==0  and a%5==0:
    print("the given number is divisible by 3 and 5")
else:
    print("the given number is not divisible by 3 and 5")








