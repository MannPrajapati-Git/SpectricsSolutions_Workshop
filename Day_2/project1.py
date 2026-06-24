# Project 1: Student Record Management System
# Problem Statement:
# Develop a command-line based Student Record Management System using core Python concepts. The system should allow users to manage student data efficiently.

# Functional Requirements:
# Your program must provide the following options:
# 1. Add a new student
# 2. Display all students
# 3. Search for a student by ID
# 4. Update student marks
# 5. Delete a student
# 6. Exit

# Mandatory Requirements:
# You must use the following data structures:

# List → to store all student records
# Dictionary → to store individual student details (id, name, marks)
# Tuple → to store fixed subject names (e.g., ("Math", "Science", "English"))
# Set → to ensure unique student IDs


# Programming Concepts:
# Use a while loop to run the program continuously
# Use if-else statements for menu selection

# Use functions for each operation


# Exception Handling:
# Handle the following errors:

# Invalid input (e.g., string instead of number)
# Duplicate student ID
# Student not found


# Optional Enhancements:

# Calculate average marks
# Display top-performing student

students = []
individual_student = {}
unique_ids=()
subjects = ("Math", "Science", "English")



def add_student():
    student_id = input("Add Student ID : ")
    student_name = (input("Add Student Name : "))
    student_marks = []
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Add marks for {subject} : "))
                if 0 <= mark <= 100:
                    student_marks.append(mark)
                    avg = sum(student_marks) / len(student_marks)
                    break
                else:
                    print("Marks should be between 0 and 100. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    for std in students:
        if std["id"] == student_id:
            print("Student ID already exists. Please try again.")
        break

    students.append({"id":student_id , "name":student_name , "marks":student_marks, "average":avg})
    print(f"the student has added successfully: {students}")
    print("------------------------------------------------------")
    



def get_individual_student():
    student_id = input("Enter Student ID : ")
    for std in students:
        if std["id"] == student_id:
            print(std)
            return
    else:
        print("Student not found.")
        print("---------------------------------------------------")

# get_individual_student()

def get_all_students():
    if not students:
        print("No students found.")
        return
    for std in students:
        print(std)
    print("---------------------------------------------------")

# get_all_students()


def update_student_marks():
    student_id = input("Enter Student ID : ")
    student_marks = []
    for std in students:
        if std["id"] == student_id:
            for subject in subjects:
                while True:
                    try:
                        mark = int(input(f"Update marks for {subject} : "))
                        if 0 <= mark <= 100:
                            student_marks.append(mark)
                            break
                        else:
                            print("Marks should be between 0 and 100. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            std["marks"] = student_marks
            print("Student marks updated successfully.")
            print("---------------------------------------------------")
                
# update_student_marks()



def delete_specific_student():
    student_id = input("Enter Student ID : ")
    for std in students:
        if std["id"] == student_id:
            students.remove(std)
            print("Student deleted successfully.")
            return
    else:
        print("Student not found.")
        print("--------------------------------------------------")

# delete_specific_student()





while True:
    print("1. Add student")
    print("2. Display all students")
    print("3. Search for a student by ID")
    print("4. Update student marks")
    print("5. Delete a student")
    print("6. Exit")
    choice = input("Enter your choice : ")
    if choice == "1":
        add_student()
    elif choice == "2":
        get_all_students()
    elif choice == "3":
        get_individual_student()
    elif choice == "4":
        update_student_marks()
    elif choice == "5":
        delete_specific_student()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
