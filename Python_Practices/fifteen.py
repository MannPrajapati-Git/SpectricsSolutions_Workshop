# 15. Take student name and 5 subject marks (list). Store total, average, and grade in a dictionary.

student = []
grade = {}

student_name = input("Enter student name: ")
for i in range(5):
    student.append(int(input("Enter subject marks: ")))
print(student)

grade = tuple(student)
print(grade)

total = sum(grade)
print("Total:", total)

average = total / 5
print("Average:", average)