# Home work
##############################
# Q5: write a python to calculate total bill and update the inventory from given
# {'FruitName': [price, inventory]}

fruits_details = {'Banana': [10, 100], 'watermelon': [60, 500], 'mango': [70, 250],
                  'Apple': [50, 100], 'lichi': [20, 300]}

fruit_purchase = {'Apple': 5, 'Banana': 10, 'watermelon': 15, 'mango': 25}
totalbill=0
for fruit,qty in fruit_purchase.items():
    #print(fruit,qty)
    #print("PRICE",fruits_details[fruit][0])
    #print("INVENTORY",fruits_details[fruit][1])
    totalfruitprice=qty*fruits_details[fruit][0]
    #print(fruit,totalfruitprice)
    totalbill+=totalfruitprice
    UpdatedInventory=fruits_details[fruit][1]-qty
    print(fruit,UpdatedInventory)
    fruits_details[fruit][1]=UpdatedInventory
print(f"The total bill is Rs.{totalbill}")
print(fruits_details)