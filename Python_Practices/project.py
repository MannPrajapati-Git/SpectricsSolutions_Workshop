# Project: Student Result Management System
# Description : Create a simple Python program that manages student results. The program will take student information, store subject marks, calculate total and average, determine the grade, and store everything in a dictionary.

# Requirements
# 1. Take student name (str).

# 2. Take 5 subject marks (int or float) from the user and store them in a list.

# 3. Convert the marks list into a tuple for fixed record storage.

# 4. Use if-else to determine the grade based on average:
# Average ≥ 75 → Grade A
# Average ≥ 60 → Grade B
# Average ≥ 50 → Grade C
# Otherwise → Fail

# 5. Store the result in a dictionary with keys:
# name
# marks
# total
# average
# grade

# 6. Use a set to remove duplicate marks (just for practice).

# 7. Use a boolean variable to check if the student passed.


student_name = input("Enter student name :")
marks = []

for i in range(5):
    marks.append(int(input(f"Enter the marks of {i + 1} subject :")))

tuple_marks = tuple(marks)
