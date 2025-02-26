# Q write a python to create diction from list of data, val will be key and square of data will the value in dict
list1 = [4, 6, 8, 1, 6, 7,4,7]
# output = {4: 16, 6: 36, 8:64, 1:1, 7:49}
dict1={}
for x in list1:
    dict1[x]=x**2
print(dict1)
print("_"*100)

#Why the below?
# if val not in output:
#Even if we have duplicate values in list the dictionary will anyway not accept duplicate key

########################################################################################

# Q2 : write a python to create dictionry from given string
# first char of each word should be key and word should be value

str1 = "Hello We Are Learning Python"
# output = {'H' : 'Hello', 'W': 'We', 'A': 'Are', 'L' : 'Learning', 'P': 'Python'}
print(str1)
dict2={}
list_words=str1.split()
for x in list_words:
    dict2[x[0]]=x
print(dict2)
print("_"*100)

########################################################################################

# Q3 : write a python to create total bill as per customer purchase from given dictionary

fruits_with_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50}
cust_pur_with_quantity = {'Apple': 10, 'Banana': 20, 'watermelon': 5, 'mango': 20}

totalbill=0
for fruit,quantity in cust_pur_with_quantity.items():
    Total_fruit_price=fruits_with_price[fruit]*quantity
    print(fruit, quantity, fruits_with_price[fruit],Total_fruit_price)
    totalbill+=Total_fruit_price
print(f"The total bill for the customer is Rs.{totalbill}")
print("_"*100)

#############################################################################################
# Q4 : write a python to calculate total bill and update the inventory

fruits_price = {'Banana': 10, 'watermelon': 60, 'mango': 70, 'Apple': 50, 'lichi': 20}
fruit_inventory = {'Apple': 100, 'Banana': 200, 'watermelon': 500, 'mango': 250, 'lichi': 300}
fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}

totalbill1=0
for fruit1,qty1 in fruit_purchase.items():
    fruit_total=qty1*fruits_price[fruit1]
    #print(fruit1,qty1,fruits_price[fruit1],fruit_total)
    totalbill1+=fruit_total
    #inventory
    #print(fruit_inventory[fruit1])
    updatedinventory=fruit_inventory[fruit1]-qty1
    #print("updated inventory: ",updatedinventory)
    fruit_inventory[fruit1]=updatedinventory

print("Total bill is: ",totalbill1)
print("Updated Inventory :",fruit_inventory)



