# 7. Take 3 boolean values (True/False) and store them in a tuple. Count how many are True.

bool_tuple = ()
bool_value1 = input("Enter first boolean value : ")
bool_value2 = input("Enter second boolean value : ")
bool_value3 = input("Enter third boolean value : ")
bool_tuple_list = []
bool_tuple_list.append(bool_value1)
bool_tuple_list.append(bool_value2)
bool_tuple_list.append(bool_value3)
bool_tuple = tuple(bool_tuple_list)
print(bool_tuple)
true_count = 0
false_count = 0
for item in bool_tuple:
    if item == True or item == "true":
        true_count += 1
    else :
        false_count +=1
print("Number of True values : ",true_count)
print("Number of False values : ",false_count)
