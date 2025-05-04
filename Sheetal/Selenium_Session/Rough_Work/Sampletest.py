print("Q1:")
def dup_name(str1):
    seen = set()
    list1 = []

    str2 = str1.split()
    for str3 in str2:
        if str3 in seen and str3 not in list1:
            list1.append(str3)

        else:
            seen.add(str3)
    output = " ".join(list1)
    return output

print("Q2:")
def find_largeword(filepath):
    with open(filepath,"w") as file:
        file.write("This is the large content file containing")

    with open(filepath, "r") as file:
        read_word= file.read()
        words = read_word.split()

        largest_word = words[0]

        for len_word in words:

            if len(len_word) > len(largest_word):
                largest_word = len_word

    return largest_word

wordnumber = find_largeword("help2.txt")

print(wordnumber)

list1 = [('mike',1),('sarah',20),('jim', 16)]

dict1 = {}

for val in list1:

    dict1[val[0]] = val[1]

print(dict1)

list1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]

index_list = [0, 3, 5, 6]

new_list = []

for value in index_list:
    new_list.append(list1[value])

print(new_list)

# rows = 5

print("Q3:")
def print_start(row):
    for i in range(row):
        if i == 0:
            print("*" * row)
        else:
            print(" " * (row // 2) + "**")

print_start(5)

print("Q4:")
Input = [2, -16, 6, 44, -71, 18, -11, -1]

# Output: [2, 6, 44, 18, -16, -71, -11, -1]

def list_arrange(nums):
    positive = []
    negative = []

    for x in nums:
        if x >= 0:
            positive.append(x)
        else:
            negative.append(x)

    num_print = positive + negative
    return num_print

num_prints = list_arrange(Input)

print("Output", num_prints)

print("Q5:")
Dict1 = { 'x':10, 'y':20, 'c':50, 'f':44 }

Dict2 = {'x':60,'c':25,'y':56}

# Output = {‘x’: 70, ‘c’: 75, ‘y’: 76}

result = { key: Dict1[key] + Dict2[key] for key in Dict1 if key in Dict2 }

Dict4 = {}
for key in Dict1:
    if key in Dict2:
        Dict4[key] = Dict1[key] + Dict2[key]

    else:
        # Dict4[key] =Dict1[key]
        break

print("Output", Dict4)