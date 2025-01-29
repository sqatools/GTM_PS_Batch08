# Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
print("-" * 60)
divisible_nums = 5, 7

for num in range(1, 50 + 1):
    if num % 5 == 0 and num % 7 == 0:
        print("From 1 to 50 divisible by 5 and 7 is :", num, end=" ")

print()
print("-" * 60)

# Q2 write a python print square of even number and cube of odd from 1 to 20

for num in range(1, 20 + 1):
    if num % 2 == 0:
        print("even number square:", num * num)
    else:
        print("odd number cube:", num * num * num)