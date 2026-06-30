# 21. Create a tuple of numbers and count how many numbers are even and odd, storing the result in a dictionary.

numbers = (10,20,30,40,50,60,70,80,90,100)
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)