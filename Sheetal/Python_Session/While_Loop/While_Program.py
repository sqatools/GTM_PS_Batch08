##Program on Reverse of Number #####

num=345
reverse = 0

while num >0:
    temp = num%10
    reverse = reverse *10 +temp
    num = num//10

print(-reverse)
print("new")

## Print all Natural Numbers

num = int(input("Enter the last no. upto which you want Natural Number to Print: "))
count=1

while count<=num:
    print(count,end=" ")
    count+=1
print("This is a list of all natural numbers upto: ",num)




