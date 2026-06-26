# 8. Create a dictionary for a student containing name and a list of marks. Calculate total, average, and grade using if-else.

student_name = input("enter student name :")
marks = []

for i in range(5):
    marks.append(int(input(f"enter the marks of {i+1} subject :")))


print("student name :", student_name)
print("marks :", marks)

total_marks = sum(marks)
average = total_marks / len(marks)

if average >= 80:
    grade = "A"
    print("Grade is : ",grade)
elif average >= 70:
    grade = "B"
    print("Grade is : ",grade)
elif average >= 60:
    grade = "C"
    print("Grade is : ",grade)
elif average >= 50:
    grade = "D"
    print("Grade is : ",grade)
else:
    grade = "Fail"
    print("Grade is : ",grade)
