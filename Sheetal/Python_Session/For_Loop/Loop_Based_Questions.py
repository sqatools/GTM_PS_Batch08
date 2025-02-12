### To check number is Prime or not
enter_num=int(input("Enter the number up to which you want to find the Prime numbers: "))
prime = True
for num in range(1,enter_num):
    if num < 2:  # 0 and 1 are not prime numbers
        continue
    prime = True
    for i in range(2,num):
        if num%i == 0:
          prime = False
          break
    if prime:
        print("The Prime number is: ", num)
print( )


print("_"*50)

### Print diamond of 5/5 size #####
"""
@@*@@
@*@*@
*@@@*
@*@*@
@@*@@
"""

for i in range(1,6):
    for j in range(1,6):
        if i==1 and j ==3:
            print("@",end =" ")
        elif (i == 2 and j == 2) or (i == 2 and j == 4):
            print("@", end=" ")
        elif (i == 3 and j == 1) or (i == 3 and j == 5):
            print("@", end=" ")
        elif (i == 4 and j == 2) or (i == 4 and j == 4):
            print("@", end=" ")
        elif (i == 5 and j == 3):
            print("@", end=" ")
        else:
            print(" ",end=" ")

    print()
###Print Diamond shape of any random number ######
"""
print("_"*50)
num_start = 10
num_rows = 10
a = num_start//2
b = num_start//2 +2

for i in range(1, num_rows+1):
    for j in range(1,num_start+1):
        if i ==1 and j == (a+1):
            print("*", end =" ")
        elif(i==2 and j==a) or (i == 2 and j == b):
          print("*", end = " ")
        elif (i == 3 and j < a) or (i == 3 and j > b):
            print("*", end=" ")
        elif (i == 4 and j == a) or (i == 4 and j == b):
            print("*", end=" ")
        elif (i == 5 and j == (a+1)):
           print("*", end=" ")
        else:
            print("",end=" ")
    print()
"""
###Print Diamond shape of any random number ######
print("_"*50)

dia_size = 11
mid = dia_size // 2


for i in range(0, mid + 1):
    for j in range(0, dia_size+1):
        if j == mid - i or j == mid + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(mid - 1, -1, -1):
    for j in range(dia_size):
        if j == mid - i or j == mid + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



