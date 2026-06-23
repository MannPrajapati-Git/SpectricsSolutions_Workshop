# list
# can have duplicate values
# run/compile - CRUD possible
# add update delete
data1 = ["a","b","c","a"]
print("List : " , data1) # List : ['a', 'b', 'c', 'a']
print("Type : " , type(data1)) # Type : <class 'list'>
print("Value Of Index 1 :" , data1[1]) # Value Of Index 1 : b

# list inbuild functions

# 1. len(list_name) : displays length
print("Length of the list is :" , len(data1))

# 2. append(value) : adds new value at the end
data1.append("H")
print(data1)

# 3. insert(index,value) : adds new value at specific index
data1.insert(4,"M")
print(data1)

# 4. remove(value) : removes specific value
data1.remove("c")
print(data1)

# 5. pop() : pop last value
k = data1.pop()
print(k)

# 6. reverse() : reverse list
data1.reverse()
print(data1)


# Tuple
# can have duplicate values
# No run/compile - CRUD possible
# No add update delete
# for CRUD you need to convert tuple into list

data2 = ("a","b","c","a")
print("Tuple : " , data2) # Tuple : ('a', 'b', 'c', 'a')
print("Type : " , type(data2)) # Type : <class 'tuple'>
print("Value Of Index 1 :" , data2[1]) # Value Of Index 1 : b

# tuple inbuild functions

# 1. len(tuple_name) : displays length
print("Length of the tuple is :" , len(data2))

# 2. count(value) : count of specific value in tuple
print("Count of a is :" , data2.count("a"))

# 3. index(value) : index of specific value in tuple
print("Index of a is :" , data2.index("a"))


# set
# can not have duplicate values
# No indexing possible
# add delete possible

data3 = {"a","b","c","a"}
print("Set : " , data3) # Set : {'a', 'b', 'c'}
print("Type : " , type(data3)) # Type : <class 'set'>

# set inbuild functions

# 1. len(set_name) : displays length
print("Length of the set is :" , len(data3))

# 2. add(value) : adds new value
data3.add("H")
print(data3)

# 3. remove(value) : removes specific value
data3.remove("b")
print(data3)

# 4. discard(value) : removes value if exists
data3.discard("x")
print(data3)

# 5. pop() : removes random value
k = data3.pop()
print(k)
print(data3)

# 6. union() : combine two sets
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))

# 7. intersection() : common values
print(set1.intersection(set2))

# 8. difference() : unique values
print(set1.difference(set2))

# 9. clear() : remove all values
temp2 = {1,2,3}
temp2.clear()
print(temp2)


# Dictionary
# key-value pair
# duplicate keys not allowed
# CRUD possible

data5 = {
    "name":"Mann",
    "age":21,
    "city":"Ahmedabad"
}

print("Dictionary : " , data5)
print("Type : " , type(data5))
print("Value Of name :" , data5["name"])

# dictionary inbuild functions

# 1. len(dict_name) : displays length
print("Length of dictionary is :" , len(data5))

# 2. keys() : displays all keys
print(data5.keys())

# 3. values() : displays all values
print(data5.values())

# 4. items() : displays key value pairs
print(data5.items())

# 5. get(key) : get value using key
print(data5.get("age"))

# 6. update() : update existing value
data5.update({"city":"Surat"})
print(data5)

# 7. add new key : add new key value pair
data5["email"] = "mann@gmail.com"
print(data5)

# 8. pop(key) : remove specific key
data5.pop("age")
print(data5)

# 9. popitem() : remove last key value pair
data5.popitem()
print(data5)

# 10. clear() : remove all data
temp3 = {
    "a":1,
    "b":2
}
temp3.clear()
print(temp3)