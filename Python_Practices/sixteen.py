# 16. Take 10 numbers from the user and store them in a list.
# Remove duplicates using set.
# Create a list of even numbers.
# Create a list of odd numbers.

user = []
for i in range(10):
    user.append(int(input("Enter a number: ")))
print(user)

user = set(user)
print(user)

even = []
odd = []
for i in user:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:", even)
print("Odd numbers:", odd)