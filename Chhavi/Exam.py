"""
str1 = "Rahul Mohit John Rahul Vaibhav John"
names = str1.split()

duplicates = []

for name in names:
    if names.count(name) > 1:
        if name not in duplicates:
            duplicates.append(name)

print("Output =", " ".join(duplicates))


x = 10

if x > 5:

    print("A")

if x > 7:

    print("B")

if x > 15:

    print("C")

else:

    print("D")

"""
"""
x = 5

if x > 3:

    if x < 7:

        print("A")

    elif x < 10:

        print("B")

elif x < 7:

    print("C")

else:

    print("D")
"""
"""

for i in range(1, 6):

       if i == 3:

           continue

       print(i)
       
"""
"""
#Q11
my_dict = {'grapes': 2, 'banana': 3, 'blue-berry': 4}

for key in my_dict:

    print(key)

"""
"""
#Q12
text = "Hello World"

#print(text.join("-"))
print("-".join(text))

"""
"""
#Q13
string = "i am learning python"

list1 = string.split(" ")

print(list1)


#Q14
list1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]

index_list = [0, 3, 5, 6]

new_list = []

for value in index_list:
    new_list.append(list1[value])

print(new_list)


#Q15
list1 = [("mike",1),("sarah",20),("jim", 16)]

dict1 = {}

for val in list1:

    dict1[val[0]] = val[1]

print(dict1)



#Q16
i = 0

while i < 15:

      print(i)

      i += 3
      


#Q17
i = 10

while True:

    print(i)

    i -= 3

    if i == 1:

        break
        


#Q18
text = "Hello World"
print(text.join("-"))



#Q19
def reverse():
    num = n = 123
    rev = 0
    while n > 0:
        r = n % 10
        rev = (rev * 10) + r
        n = n // 10
    print("Reverse number: ", rev)

reverse()


#Q20
def __init__(self):
    self.__private_var = 25


def __private_method(self):
    print("Private method")


def public_method(self):
    print("Public method")

    self.__private_method()


# Create an object of the class

obj = MyClass()

# Access public method and variable

obj.public_method()

print(obj._MyClass__private_var)


#Q4

Num1 = [2, -16, 6, 44, -71, 18, -11, -1]

positive_numbers = []
negative_numbers = []

for num in Num1:
    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)

result = positive_numbers + negative_numbers
print(result)



#Q5
Dict1 = {'x': 10, 'y': 20, 'c': 50, 'f': 44}
Dict2 = {'x': 60, 'c': 25, 'y': 56}

result = {}

for key in Dict1:
    if key in Dict2:
        result[key] = Dict1[key] + Dict2[key]

print(result)

"""

#Q2
with open("example.txt", "w") as file:
    file.write("Python is difficult but interesting to learn.")

with open("example.txt", "r") as file:
    content = file.read()

words = content.split()
longest_word = max(words, key=len)

print("The longest word is:", longest_word)
