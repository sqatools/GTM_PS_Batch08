print("*"*15,"print a string five times", "*"*15)
a = str(input("String to print: "))
t=1
while t < 6:
    print(a)
    t=t+1
print()
#***************************************************************************
print("*"*15,"Program to find even and odd numbers form a given series", "*"*15)
bucket = (1,3,2,4,6,7,8,9,12,54,31)
eve = 0
odd= 0

for i in bucket:
    if i%2==0:
        eve=eve+1
    else:
        odd=odd+1
print("No. of even:",eve)
print("No. of odd:", odd)
print()


#*******************************************************************************
print("*"*15,"Program to find average marks and percentage of marks of 5 subjects", "*"*15)
m=78
e=67
h=77
sst=86
sc=85
Tot_marks = m+e+h+sst+sc
print("maths=78, English=67, Hindi=77, sst=86, sc=85")
print("total marks:", Tot_marks)
print("Average marks:", Tot_marks/5)
print("Percentage:", (Tot_marks/500)*100)
if ((Tot_marks/500)*100)>=60:
    print("First Division")
elif((Tot_marks/500)*100)<60 and ((Tot_marks/500)*100)>=40:
    print("Second Division")
else:
    print("Fail")
print()
#*******************************************************************************
print("*"*15,"Print * in a pyramid shape", "*"*15)
n = int(input("number of lines for pyramid: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        print("*",end="")
    print()

#********reverse a nummber*
num=121
var1=num
reverse=0
while num>0: #123>0, 12>0, 1>0
    temp=num%10 #3
    reverse=reverse*10+temp #3
    num=num//10  #12 12,1,0
print(reverse)

if var1==reverse:
    print("This is a palindrom",reverse)
else:
    print("This is not palindrom",reverse)
