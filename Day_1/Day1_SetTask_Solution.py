# Set Tasks
# 1. Create a set of 5 unique numbers.
# 2. Add a new element to a set using add().
# 3. Remove an element from a set using remove().
# 4. Check if a value exists in a set.
# 5. Create two sets and find their union.
# 6. Find the intersection of two sets.
# 7. Create a set and convert it to a list.
# 8. Remove all elements from a set using clear().
# 9. Find the difference between two sets.
# 10. Add multiple elements to a set using update().

# 1.
set1 = {1,2,3,4,5}
print(set1)

# 2.    
set1.add(6)
print(set1)

# 3.
set1.remove(3)
print(set1)

# 4.
if 4 in set1:
    print("Value exist")

# 5.
set2 = {7,8,9,10}
set3 = set1.union(set2)
print(set3)

# 6.
set4 = set1.intersection(set2)
print(set4)

# 7.
list1 = list(set1)
print(list1)

# 8.
set1.clear()
print(set1)

# 9.
set5 = {11,12,13,14}
set6 = {15,16,17,18}
set7 = set5.difference(set6)
print(set7)

# 10.
set5.update(set6)
print(set5)