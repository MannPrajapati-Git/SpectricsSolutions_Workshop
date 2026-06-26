# 1. Take name (str), age (int), height (float), and is_student (bool) as input. Use if-else to determine whether the person is an Adult or Minor.

name = input("Enter Name: ")
age = int(input("Enter Age: "))
height = float(input("Enter Height: "))
is_student = input("Are you a student? (True/False): ")

if age >= 18:
    status = "Adult"
else:
    status = "Minor"

print(f"{name} is a {status}.")
