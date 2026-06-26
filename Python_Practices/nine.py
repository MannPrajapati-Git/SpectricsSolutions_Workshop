# 9. Take 5 items from the user and store them in a list. Convert the list into a set to remove duplicates and print the number of unique items.

item = []

for i in range(5):
    item.append(input("enter the item : "))
    
item_set = set(item)
print("Total number of items is : ",len(item))
print("Unique items are : ",item_set)
print("number of unique items : ",len(item_set))