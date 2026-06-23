# List Tasks
# 1. Create a list of 5 colors and print it.
# 2. Add a new item to a list using append().
# 3. Remove an item from a list using remove().
# 4. Find the length of a list using len().
# 5. Print the first and last element of a list.
# 6. Replace the third element in a list with a new value.
# 7. Sort a list of numbers.
# 8. Count how many times a value appears in a list.
# 9. Create a list of 5 numbers and print the maximum number.
# 10. Reverse a list without using slicing.

# 1.
colors = ["red", "pink", "black", "blue", "green"]
print(colors)

# 2.
colors.append("purple")
print(colors)

# 3.
colors.remove("black")
print(colors)

# 4.
length = len(colors)
print(length)

# 5.
print("First Element : ", colors[0] ,"And","Last Element :",colors[4])

# 6.
colors.insert(2,"Gray")
print(colors)

# 7.
numbers = [54,76,12,90,34,23]
numbers.sort()
print(numbers)

# 8.
colors.append("blue")
colors.append("blue")
item = colors.count("blue")
print(item)

# 9.
print("Max number is : ",max(numbers))

# 10.
numbers.reverse()
print(numbers)