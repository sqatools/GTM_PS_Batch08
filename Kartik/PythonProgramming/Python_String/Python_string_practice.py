###### String Formatting ###############

name = 'Kartik'
age = 28
city = " Surat"

# Hello My name is kartik and age is 28, and I am living in surat

print('_' * 50)
# 1) String Concatenation
"""
result1 = "My name is " + name + " and age is " + age  + " and i living in " +city 
# in age TypeError: can only concatenate str (not "int") to str
"""
result1 = "My name is " + name + " and age is " + str(age) + " and i living in " + city

print(result1)
print('_' * 50)
# 2) String Formatting

result2 = "Hello my name is {} and age is {} and i living in {}".format(name, age, city)
print(result2)

print('_' * 50)
# 3) F String Formatting
result3 = f"Hello my name is {name} and age is {age} and i living in {city}"

print(result3)

print('_' * 50)
# ---------------Raw String Conversion -----------------------
str2 = " Hello Good morning.\twe are learning Python  \n programming .\n \n it is very easy to learn"
str3 = r" Hello Good morning.\twe are learning Python  \n programming .\n \n it is very easy to learn"

print(str2)

print('_' * 50)
print(str3)
"""
Note : \t = for adding tab spaces in string
       \n = adding next line output
Note : when we add r before the double quote (") then entire string will convert in to raw string.
       All Special character properties won't work e.g \t and \n
    
"""
print('_' * 50)
# -----------Slicing in the String -----------------------

"""
str [start index : End index]
Rules : - sub string will include start index value and exclude end index value.
        - output will always consider the string value from left to right ( Left --> Right)
        - It can contain both positive and negative index values.

"""

print('_' * 50)
str_a = 'Transaction'
"""
 (1) - [ +ve :+ve ] 
"""
print(str_a[2:7])

print('_' * 50)
"""
 print(str_a[7:2])      # as per rules right to left is not possible ,it gives blank output
 
                        if we try to get values from right to left then it will return blank output
 
 """
print(str_a[0:9])
print('_' * 50)
"""
 (2) - [ +ve :-ve ] 
"""
print(str_a[2:-2])
print('_' * 50)
print(str_a[1:-1])

print('_' * 50)
"""
 (3) - [ -ve :+ve ] 
"""
str_b = "Python programming"
print(str_b[-9:12])

print('_' * 50)
"""
 (4) - [ -ve :-ve ] 
"""
print(str_b[-13: -3])

#--- Home work --
str_c = "Learning Python"
str_d = 'India is best Country'

print('_' * 50)
"""
Q-1 Read only "Learning"
"""
print(str_c[0:8]) # Learning
"""
Q-2 Read only First Character and last character "Ln"
"""
str_1 = (str_c[0])
#print(str_1)
str_2 = (str_c[-1])
#print(str_2)
output = ""+str_1+""+str_2
print(output) # Ln
output1 = f"{str_1}{str_2}"
print(output1) # Ln

#print(str_c[0],str_c[-1])

"""
Q-3 Read  All character except First character and last character and repeat 2 times "earning Pythoearning Pytho" 
"""
print((str_c[1:-1])*2)
"""
Q-4 Read  All character except First character and last character and repeat 2 times "earning Pythoearning Pytho" 
"""
strfc =str(str_c[0])
#print(strfc)
strlc =str(str_c[-1])
#print(strlc)

finalstr = ""+strfc+""+str_c+""+strlc

print(finalstr)


#print((str_c[1:-1])*2) # LLearning Pythonn



