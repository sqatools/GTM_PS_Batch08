num1=int(input("Enter number: "))
rev1=0
while num1>0:
    temp=num1%10
    rev1=rev1*10+temp
    num1=num1//10
print(rev1)

