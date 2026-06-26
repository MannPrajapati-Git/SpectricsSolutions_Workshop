# 2. Take 5 numbers from the user and store them in a list. Separate them into even numbers list and odd numbers list.

nummbers = []
for i in range(5):
    num = int(input("Enter number : "))
    nummbers.append(num)

even = []
odd = []
for num in nummbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)