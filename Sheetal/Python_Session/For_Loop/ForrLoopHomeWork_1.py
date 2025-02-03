## Python Loops program to construct the following pattern, using a nested for loops.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
num = int(input("Enter number of rows for pattern number"))

for i in range(0,num):  ##rows
    for k in range(0,i+1):  ##column
        print("*",end=" ")
    print()
for i in range(0, num):
    for j in range(i,num):
         print("*",end=" ")
    print()



"""print("_"*40)
for i in range(num-1,0):
    for j in range(0,i+1):
         print("*",end=" ")
    print()
for i in range(0,num):  ##rows
    for k in range(i,num//2):  ##column
        print("*",end=" ")
    print()
"""
## Full Diamond

print("_"*40)
num = int(input("Enter number of rows for the pattern: "))

# Upper part of the diamond
for i in range(1, num + 1):
    print(" " * (num - i) + "* " * i)


# Lower part of the diamond
for i in range(num - 1, 0, -1):
    print(" " * (num - i) + "* " * i)

##Python for loop program to print the alphabet pattern 0 using python.
"""Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  
"""
for i in range(0,13):
    for j in range(0,13):
        if (i==0 or i==12) and (1< j <11):
            print("*",end=" ")
        elif(0< i <=11) and (j==1 or j==11):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()