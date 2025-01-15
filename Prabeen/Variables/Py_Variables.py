a = 10
print(a)

print(id(a))

x = 20
y = 20

# if two variable have same value, thn their address will same
print("x vale is", x, "and it's address is", id(x))
print("y vale is", y, "and it's address is", id(y))

#Assign multiple values at a time
p, q, r = 50, 60, 70
print("value of p, q, r is", p, q, r)

#Assign same value to multiple variables
A = B = C = 100
print("Value of A is ", A, "Address is ", id(A))
print("Value of B is ", B, "Address is ", id(B))
print("Value of C is ", C, "Address is ", id(C))

#Python is case-sensitive, variable name will treat differently with different case-sensitive
Name = 'Jai'
NAME = 'Rahul'
name = 'Mohit'
namE = 'Pramod'
print(Name, NAME, name, namE)

print(Name, "\n", NAME, "\n", name, "\n", namE)

#To print all the keywords available
import keyword
print(keyword.kwlist)

