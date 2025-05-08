# write a python to create dictionary from list of data, val will be key and squaare of data  will the value

list1 = [4, 6, 8, 1, 6, 7]
output = {}

for val in list1:
    if val not in output:
        output[val]=val**2
    else:
        continue

print("output :", output)
# output : {4: 16, 6: 36, 8: 64, 1: 1, 7: 49}


# 2) write a python program to create dictionary from given string
# first char of each word should be and word should be value

str1 = " hi whatsapp"

output = {}
word_list = str1.split()
print(word_list)
# ['hi', 'whatsapp']
for word in word_list:
    output[word[0]] = word

print("output :", output)
#  {'h': 'hi', 'w': 'whatsapp'}
print("_"*50)
#################################
# 3) write a python program to create total bill as per customer purchase from given dictionary

fruits_with_price = {'cake': 10, 'biscuit': 60, 'bread': 70, 'chocolate': 50}
cust_purchase_with_quantity = {'chocolate': 50, 'cake': 10, 'biscuit': 60, 'bread': 70}
total_bill = 0
for fruit,quant in cust_purchase_with_quantity.items():
    fruit_price = fruits_with_price[fruit]
    total_bill = total_bill+fruit_price*quant

print("total bill :", total_bill)
# total bill : 11100

print("_"*50)
# 4) write a python program to calculate total bill and update the inventory

fruits_price = {'cake': 10, 'biscuit': 60, 'bread': 70, 'chocolate': 50}
fruit_inventory = {'chocolate' : 20, 'cake' : 30, 'biscuit' : 35, 'bread': 40}
fruit_purchase = {'chocolate': 50, 'cake': 10, 'biscuit': 60, 'bread': 70}

for fruit, pur_quant in fruit_purchase.items():
    fruit_name = fruit
    fruit_pur_quant = pur_quant
    fruit_price = fruits_price[fruit]
    fruit_bill = fruit_pur_quant*fruiti_price
    total_bill = total_bill + fruit_bill
    print("fruit name:", fruit_name)
    print("fruit_purchase quant:", fruit_pur_quant)
    print("fruit price :", fruit_price)
    print("fruit bill :", fruit_bill)
    print("_" * 40)

print("total bill amount :", total_bill)