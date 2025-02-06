#------------Write a program or fibonacci series 0-20--------------------------

num1 =0
num2 = 1
count = 0

while count<20:
    print(num1, end=" ")
    n2=num1+num2
    num1=num2
    num2=n2
    count = count+1


#---------------Prime number 0r not--------------------

num1 = int(input("Enter number : "))
count=0

for i in range(2,num1):
    if num1%i == 0:
        count = count + 1

if count>0:
    print("not Prime number")
else:
    print("Prime number")

