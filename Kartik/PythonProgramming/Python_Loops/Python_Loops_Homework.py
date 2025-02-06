"""
1. Write a python program to print value which are divisible 5 and 7 from 1 to 50.
"""
num1 = 5
num2 = 7
for i in range(1, 50):
    if (i % num1) == 0 or  (i % num2) == 0:
        print(i)
    #elif (i % num2) == 0:
      #  print(i)
print(i)

print("_" * 50)

"""
2. Write a python program to print square of even number and cube of odd number from 1 to 20.
"""
for j in range(1, 21, 1):

    if (j % 2) == 0:
        print(i ** 2)
    else:
        print(i ** 3)
