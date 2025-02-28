# Q write a python to create diction from list of data, val will be key and square of data
# will the value in dict
# output = {4: 16, 6: 36, 8:64, 1:1, 7:49}

listA = [4, 6, 8, 1, 6, 7]
dictA = {}

for val in listA:
    if val not in dictA:
        dictA[val] = val ** 2
    else:
        continue
print(dictA)
print("_"*50)


# 2. write a python to create dictionary from given string
#    first char of each word should be key and word should be value

str1 = "Hello We Are Learning Python"
# output = {'H' : 'Hello', 'W': 'We', 'A': 'Are', 'L' : 'Learning', 'P': 'Python'}

str2 = str1.split()
# print(str2)
out = {}

for word in str2:
    # print(word,":",word[0])
    out[word[0]] = word
print("The dictionary that is formed is:")
print(out)
print("_"*50)


# 3. write a python to create total bill as per customer purchase from given dictionary

fruits_with_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50}
cust_pur_with_quantity = {'Apple': 10, 'Banana': 20, 'watermelon': 5, 'mango': 20}

totalBill = 0
for k, v in cust_pur_with_quantity.items():
    fruitPrice = fruits_with_price[k]  # get each fruit price
    fruitBill = fruitPrice * v   # get each fruit bill
    print(k, v, fruitPrice, fruitBill)
    totalBill = totalBill + fruitBill

print("Total Bill as per customer purchase is: ",totalBill)
# print(fruits_with_price['Apple'])
print("_"*50)


# 4 : write a python to calculate total bill and update the inventory
fruits_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50, 'lichi': 20}
fruit_inventory = {'Apple': 100, 'Banana': 200, 'watermelon': 500, 'mango': 250, 'lichi': 300}
fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}

totalBill = 0

for fruit, purQuant in fruit_purchase.items():
    fruitName = fruit
    fruitPurQuant = purQuant
    fruitPrice = fruits_price[fruit]
    fruitBill = fruitPurQuant * fruitPrice
    totalBill = totalBill + fruitBill
    updateInventoryVal = fruit_inventory[fruit] - fruitPurQuant
    fruit_inventory[fruit] = updateInventoryVal

    print("Fruit name :",fruitName)
    print("Fruit Purchase Quantity :",fruitPurQuant)
    print("Fruit Price: ",fruitPrice)
    print("Bill of that Fruit: ",fruitBill)
    print("Fruit Inventory: ",fruit_inventory[fruit])
    print("Updated fruit inventory: ",updateInventoryVal)
    print("_" * 40)

print("Total Bill of all fruits is: ",totalBill)
print("_"*70)


# Q5: write a python to calculate total bill and update the inventory from given
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25, 'lichi': 25}

totalBill = 0
for k, v in fruit_purchase.items():
    fruitPrice = v * fruits_details[k][0]
    print(k,":", v,":", fruitPrice) # Fruit : quantity purchased : price of total fruits of that kind
    totalBill = totalBill + fruitPrice
    fruits_details[k][1] = fruits_details[k][1] - v

print("Total Bill :",totalBill)
print("The updated Inventory is: ",fruits_details)
print("_"*70)







