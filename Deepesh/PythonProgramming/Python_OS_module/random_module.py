import random

# get any random number from 1 to 10
print(random.randint(1, 10))

# get random value
print(random.random()) # 0.5844685452998718

# randrange return the random value from given range.
print("random range value:", random.randrange(1, 20, 2))


# random shuffle the list values
list1 = [4, 6, 8, 7, 1, 9]
random.shuffle(list1)
print(list1) # [6, 9, 7, 8, 1, 4]


# get random choice from list values
list2 = [5, 7, 9, 23, 55, 77, 8]
print(random.choice(list2)) # # 8
