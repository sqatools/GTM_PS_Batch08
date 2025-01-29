#Q1 write a python program to print value which are divisible 5 and 7 from 1 to 50
print("="*50)
print("To print value which are divisible by 5 and 7 from 1 to 50")
print("-"*50)
for i in range(1, 51):
    if i%5==0 and i%7==0:
        print("The value which is divisible by 5 and 7 is: ", i)

#Q2 write a python print square of even number and cube of odd from 1 to 20

print("=" * 50)
print("To check cube of add numbers and square of even numbers")
#print("ODD    \t  EVEN")
print("-------------------------")
for j in range(1, 21):
    if j%2 == 0:
        print("Even number of ", j, " is : ", j**2)
    else:
        print("odd number of ", j, " is : ", j**3, end=" ; ")


