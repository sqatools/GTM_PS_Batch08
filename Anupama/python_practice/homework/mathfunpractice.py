#******(a+b)^3 = a^3 + b^3 + 3ab(a+b)
print("Calculate answer for (a+b)^3")
a = int(input("Integer value of a: "))
b = int(input("integer value of b: "))
print(a)
print(b)
cal= (a**3) + (b**3) + ((3*a*b)*(a+b))
print("Answer for (a+b)^3= ", cal)

#*****(a-b)(a+b) = a^2 - b^2

print("Calculate answer for (a-b)(a+b)" )
a = int(input("Integer value of a: "))
b = int(input("integer value of b: "))
cal= (a**2) - (b**2)
print("Answer for (a-b)(a+b) =", cal)

#*****a3-b3 = (a-b)^3 + 3ab(a-b)
print("**** a3-b3 = (a-b)^3 + 3ab(a-b)")
print("Calculate answer for a^3-b^3" )
a = int(input("Integer value of a: "))
b = int(input("integer value of b: "))
cal= (((a-b)**3) +(3*a*b)*(a-b))
print("Answer for (a-b)(a+b) =", cal)

#**** calculate area of circle a= pi*r^2
pi=3.14
r=4
print("pi = 3.14")
print("r = 4")
area= pi*r**2
print("area of circle is:", area)

# ***Python program to convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

