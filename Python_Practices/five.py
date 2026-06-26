# 5. Take 10 numbers in a list and convert the list to a set to remove duplicates. Print the unique numbers.

nummbers = []
for i in range(10):
    num = int(input("Enter number : "))
    nummbers.append(num)

unique = set(nummbers)
print("Unique numbers:", unique)