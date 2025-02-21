#  20). Write a program to find the first and last digits of a number using python.
num = 12345
num1 = str( num )
for i in range( len( num1 ) ):
    if i == 0:
        print( f"first digit is:{num1[i]}" )
    elif i == len(num1)-1 :
        print(f"last digit is:{num1[i]}")

