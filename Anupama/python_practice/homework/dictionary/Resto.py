print("*****Welcome to Anu's Resto*****" )
print("***Menu***")
print("\n1)Pizza: 40\n2)Pasta: 50\n3)Burger: 55\n4)Salad: 70\n5)Coffee: 80\n6)Tea: 60\n7)Maggi:70")

tot_ord=0
item_1= input("Enter the item from the menu:")
if item_1 in menu:
      tot_ord=tot_ord+menu[item_1]
      print(f"your item {item_1} has  been added to order")

else: print("Ordered item is not available")

another_item = input("Do you want another item?(y/n)")
if another_item == "Y" or "y" or "Yes" or "yes":
      item_2 = input("Enter another item from the menu:")
      if item_2 in menu:
            tot_ord = tot_ord+menu[item_2]
            print(f"your item {item_2} has  been added to order")
      else:
            print("Ordered item is not available")
            print(f"Total amount to pay {tot_ord}")
else:
      print("Thank you. ")
      print(f"Total amount to pay {tot_ord}")