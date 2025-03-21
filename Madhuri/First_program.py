# Day  : 05 the March 2025

#definition:
a = 20
print("Value of a: ", a)
print("Address of a : ", id(a))

b = 5
c = 5
b= c = 5
print("Value of b:", b , "Address ob b:", id(b))
print("Value of c:", c , "Address ob c:", id(c))

print("#"*50)
p,q,r = 3, 4,5
print(p)
print(q)
print(r)
print(p,q,r)

print("#"*50)


#l=25
#print(L) # Syntax Error
# Python is Case Sensitive Lang

# Rules used in Variable:
# 1. Cannot start with NUmber, Special char And can start with a/A  Ex: 23AA = 50
# 2. Space not allowed in the variable name  Ex: My Age = 25
# 3. No limit length Ex. aaaaadddddddddeeee = 10
# 4. Case sensitive
# 5. Special char not allowed in the variable name except Underscore (_)
# 6 variable name shpuld not be bollen values True/False


# Math Operations: +,-, *, /, //, %, **, ==, !=
n1 = -25.3
n2 = 3.7
print("Add:", n1+n2)
print("Sub", n1-n2)
print("Multi ", n1*n2)
print("Div ", n1/n2)  # Consider floating value
print("Div ", n1//n2) # Consider Integer value
print("Mod ", n1%n2)
print("Square ", n1**2)
print("Cube ", n2**3)
print("Equal To ", n1==n2)
print("Not Equal To ", n1!=n2)



a1 = b1 = c1 = 10
a2,b2,c2  = 15 ,23,45


num = 2.789
print(round(num))

num1 = 2.999
print(round(num1))