# 10. Create a tuple of numbers and print all numbers greater than 30.

# numbers = (10,20,30,40,50,60,70,80,90,100)
numbers = []

for i in range(10):
    numbers.append(int(input("Enter the number : ")))

num_tuple = tuple(numbers)

print(" Tuple is :",num_tuple)
for i in num_tuple:
    if i > 30:
        print("Numbers greater than 30 are :",i)
