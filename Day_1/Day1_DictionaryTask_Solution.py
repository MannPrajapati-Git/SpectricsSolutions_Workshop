# Dictionary Tasks
# 1. Create a dictionary with 3 key-value pairs and print it.
# 2. Add a new key-value pair to a dictionary.
# 3. Remove a key from a dictionary using pop().
# 4. Print all keys of a dictionary.
# 5. Print all values of a dictionary.
# 6. Update the value of an existing key.
# 7. Check if a key exists in a dictionary.
# 8. Create a dictionary and print the number of items.
# 9. Create a dictionary and print only the keys.
# 10. Merge two dictionaries into one.

# 1.
dict1 = {"name":"Mann", "age":21, "city":"Ahmedabad"}
print(dict1)

# 2.
dict1["country"] = "India"
print(dict1)

# 3.
dict1.pop("city")
print(dict1)

# 4.
print(dict1.keys())

# 5.
print(dict1.values())

# 6.
dict1["age"] = 22
print(dict1)

# 7.
if "name" in dict1:
    print("Value exist")

# 8.
print(len(dict1))

# 9.
print(dict1.keys())

# 10.
dict2 = {"name1":"Heli", "age1":22, "city1":"Ahmedabad"}
dict1.update(dict2)
print(dict1)