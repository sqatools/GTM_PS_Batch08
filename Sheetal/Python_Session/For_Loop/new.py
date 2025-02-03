##Prime Number
num=int(input("Enter the number up to which you want to find list: "))

for i in range(2,num+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                  break
        else:
            print("This is a prime number", i)

print("_"*50)
##Fibonacci Series

a,b=0,1
for i in range(num):
    print(a,end=" ")
    a,b=b,a+b
print()
print("This is the Fibonacci series upto the number", num)

print("_"*50)
## Reverse of a Number
num1=num
reverse=0
for i in range(0,num):
    if num>0:
        temp=num%10
        reverse=reverse*10+temp
        num=num//10
print("The reverse of number",num1 , "is: ",reverse)

num=num1
print(num,"The original number")

print("_"*50)
## Diamond Pattern
for i in range(1,num+1):
    print(" " * (num-i) + "*" * (2* i-1))
for j in range(num-1,0,-1):
    print(" " * (num-j) + "*" * (2* j-1))

print("_"*50)
##Second method to print Diamond Pattern
d_size=num//2

for i in range(1,d_size+2):
    for j in range(0,num):
        if (j == d_size-i+1) or (j == d_size+i-1):
            print("*",end=" ")
        else:
            print(" ", end= " ")
    print()
for i in range(d_size,0,-1):
    for j in range(0,num):
        if (j == d_size-i +1) or (j == d_size+i-1):
            print("*",end=" ")
        else:
            print(" ", end= " ")
    print()


print("_"*50)
## To print Even and Odd Number
for i in range(0,num+1):
    if i%2 == 0:
        print("This is an even number: ", i)
    else:
        print("This is not an odd number: ", i)


## Print Number is a Palindrome Number
num = int(input("Enter a number"))
reverse = 0
num1 = num
str_num = str(num)
num_len = len(str_num)

for i in range(num_len):
    if num>0:
        temp=num%10
        reverse = reverse*10 +temp
        num = num//10

print("The entered number is: ",num1)

if num1==reverse:
    print("The entered number is a Palindrome number: ", reverse)
else:
    print("The entered number is not a Palindrome number", reverse)

