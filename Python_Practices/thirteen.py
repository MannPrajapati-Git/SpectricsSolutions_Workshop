# 13. Store 10 integers in a list. Count how many numbers are positive, negative, and zero.

numbers = []
positive = 0
negative = 0
zero = 0

for i in range(10):
    numbers.append(int(input("Enter the number : ")))

print("List of numbers : ",numbers)

for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1

print("Positive numbers : ",positive)
print("Negative numbers : ",negative)
print("Zero numbers : ",zero)
