# Q write a python to create diction from list of data, val will be key and square of data will the value in dict

list1 = [4, 6, 8, 1, 6, 7]
# output = {4: 16, 6: 36, 8:64, 1:1, 7:49}
output = {}

for val in list1:
    if val not in output:
        output[val] = val ** 2
    else:
        continue

print("output :", output)
# {4: 16, 6: 36, 8: 64, 1: 1, 7: 49}


# Q2 : write a python to create dictionry from given string
# first char of each word should be key and word should be value

str1 = "Hello We Are Learning Python"
# output = {'H' : 'Hello', 'W': 'We', 'A': 'Are', 'L' : 'Learning', 'P': 'Python'}

output = {}
word_list = str1.split()
print(word_list)
# ['Hello', 'We', 'Are', 'Learning', 'Python']

for word in word_list:
    print(word, ":", word[0])
    output[word[0]] = word

print("output :", output)
# {'H': 'Hello', 'W': 'We', 'A': 'Are', 'L': 'Learning', 'P': 'Python'}

dict2 = {}
dict2['a'] = 'Hello'

print("_" * 50)
##############################
# Q3 : write a python to create total bill as per customer purchase from given dictionary

fruits_with_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50}
cust_pur_with_quantity = {'Apple': 10, 'Banana': 20, 'watermelon': 5, 'mango': 20}

total_bill = 0

for k, v in cust_pur_with_quantity.items():
    # get each fruit price
    fruit_price = fruits_with_price[k]
    # get each fruit bill
    fruit_bill = v * fruit_price
    # print fruit_name, fruit_quant, fruit_price, fruit_bill
    print(k, v, fruit_price, fruit_bill)
    # all each fruit bill into total bill
    total_bill = total_bill + fruit_bill

print("Total bill amount :", total_bill)

print(fruits_with_price['Apple'])

# for fruit, quant in cust_pur_with_quantity.items():
#     fruit_price = fruits_with_price[fruit]
#     # fruits_with_price['Apple']
#     print(fruit, "|", fruit_price,"|", quant)
#     total_bill = total_bill + fruit_price*quant
#
# print("Total bill :", total_bill)


print("#" * 50)
##############################
# Q4 : write a python to calculate total bill and update the inventory

fruits_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50, 'lichi': 20}
fruit_inventory = {'Apple': 100, 'Banana': 200, 'watermelon': 500, 'mango': 250, 'lichi': 300}
fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}
total_bill = 0
for fruit, pur_quant in fruit_purchase.items():
    fruit_name = fruit
    fruit_pur_quant = pur_quant
    fruit_price = fruits_price[fruit]
    fruit_bill = fruit_pur_quant*fruit_price
    total_bill = total_bill + fruit_bill
    fruit_inventory_val = fruit_inventory[fruit]
    updated_inventory_val = fruit_inventory_val - fruit_pur_quant
    # updated_inventory_val = fruit_inventory[fruit] - fruit_pur_quant
    fruit_inventory[fruit] = updated_inventory_val
    print("Fruit name:", fruit_name)
    print("Fruit Purchase Quant:", fruit_pur_quant)
    print("Fruit Price :", fruit_price)
    print("Fruit Bill :", fruit_bill)
    print("Fruit inventory :", fruit_inventory_val)
    print("Fruit updated inventory :", updated_inventory_val)
    print("_" * 40)

print("Total Bill Amount :", total_bill)
print(fruit_inventory)


# Home work
##############################
# Q5: write a python to calculate total bill and update the inventory from given
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}

print("_"*50)

total_bill=0

for fruit, quant in fruit_purchase.items():
    fruit_charges = quant*fruits_details[fruit][0]
    total_bill= total_bill + fruit_charges
    fruits_details[fruit][1]=fruits_details[fruit][1]-quant

print(fruits_details)
print(total_bill)


