# Homework and Practice Questions :

#1. write a python program to print value which are divisible 5 and 7 from 1 to 50
print("1. Write a python program to print value which are divisible 5 and 7 from 1 to 50")
print("Numbers from 1-50 that are divisible by both 5 and 7")
for i in range(1, 50, 1):
    if i %5 == 0 and i % 7 == 0:
        print(i, end=",")
print()
print("_"*80)

#2 write a python program to print square of even number and cube of odd from 1 to 20
print("#2. Write a python program to print square of even number and cube of odd from 1 to 20")
for i in range (1, 21, 1):
    if i %2 == 0:
        print(i," is even number so square of the number is: ",i**2)
    else:
        print(i," is odd number so cube of the number is: ",i**3)
print("_" * 80)



