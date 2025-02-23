# str formatting
name = "Madhuri"
age = 25
city = 'Pune'
# Output should be: Hello My name is Madhuri and my age is 25 and I am living in Pune

# 1) Str Concatination :
result1 = "Hello My name is " + name + " and my age is " + str(age) + " and I am living in " + city
print(result1) #Hello My name is Madhuri and my age is 25 and I am living in Pune


print("#"*40)
# 2) Str Formating :
#result2 = "Hello My name is {} and my age is {} and I am living in {}".format(name,age,city)
#print(result2) #Hello My name is Madhuri and my age is 25 and I am living in Pune

#result2 = "Hello My name is {} and my age is {} and I am living in {}".format(name,city)
#print(result2) #IndexError: Replacement index 2 out of range for positional args tuple

result2 = "Hello My name is {} and my age is {} and I am living in {}".format(city,name,age)
print(result2) #Hello My name is Pune and my age is Madhuri and I am living in 25


# iii) f string formatting
result3 = f"Hello My name is {age} and my age is {name} and I am living in {city}"
print(result3) #Hello My name is 25 and my age is Madhuri and I am living in Pune

print("#"*50)

# Raw String Conversion

# we used r here, so tab or new line function will be not consider and will consider whole raw string only
#str1 = r"Hello good \n \t morning, we \t are learing pPython language \t \t programming, its very easy \n \n \t \nlanguage"
#print(str1) #Hello good \n \t morning, we \t are learing pPython language \t \t programming, its very easy \n \n \t \nlanguage


# we havent used r here, so tab or new line function will consider here
#str1 = "Hello good \n \t morning, we \t are learing pPython language \t \t programming, its very easy \n \n \t \nlanguage"
#print(str1)
"""Output:
Hello good 
 	 morning, we 	 are learing pPython language 	 	 programming, its very easy 
 
 	 
language
"""

print("#"*50)
#Slicing in the  String:
# Rule1 :
# str[start index : end index]
# output display in str from left to Right
# Contains both positive and negative index value

strA = "Programming"
#[+:+]
print (strA[4:7]) #ram

#[+,-]
print(strA[2:-2]) #ogrammi

#[-,+]
print(strA[-7:10]) #rammin

#[-,-]
print(strA[-9:-2]) #ogrammi




