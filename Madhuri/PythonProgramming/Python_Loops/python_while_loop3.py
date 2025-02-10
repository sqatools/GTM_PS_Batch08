# ASCII Values :
# A-Z : 65-90
# a-z : 97-122

# chr() : this function will return the character if we provide the ASCII value
print(chr(65))  # A

# ord() : This return the ASCII value of we provide the character.
print(ord("B")) # 66

for i in range(65, 91):
    print(chr(i), end=" ")
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

print()

for i in range(97, 123):
    print(chr(i), end=" ")
# a b c d e f g h i j k l m n o p q r s t u v w x y z


print()
print("_"*50)

start_value = 65
for i in range(1, 8):
    for j in range(i):
        print(chr(start_value), end=" ")
        start_value += 1
    print()

# print(chr(91))

str1 = "Hello"
str1.upper()

print(chr(65).lower())
