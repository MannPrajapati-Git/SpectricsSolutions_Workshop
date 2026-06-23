# Tuple Tasks
# 1. Create a tuple of 5 fruits and print it.
# 2. Print the second and fourth element of a tuple.
# 3. Find the length of a tuple.
# 4. Check if a value exists in a tuple.
# 5. Convert a tuple into a list.
# 6. Convert a list into a tuple.
# 7. Find the index of an element in a tuple.
# 8. Count how many times a value appears in a tuple.
# 9. Join two tuples together.
# 10. Print the last element of a tuple using negative indexing.

# 1.
fruits = ("mango", "banana", "orange", "apple", "grapes")
print(fruits)

# 2.
print(fruits[1], fruits[3])

# 3.
length = len(fruits)
print(length)

# 4.
if("apple" in fruits):
    print("Value exist")

# 5.
list_fruits = list(fruits)
print(list_fruits)

# 6.
tuple_fruits = tuple(list_fruits)
print(tuple_fruits)

# 7.
index = fruits.index("apple")
print(index)

# 8.
count = fruits.count("apple")
print(count)

# 9.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2
print(tuple3)

# 10.
print(fruits[-1])