students = []
unique_ids = set()
subjects = ("Math", "Science", "English")


def add_student():
    student_id = input("Enter Student ID: ")

    if student_id in unique_ids:
        print("Error: Student ID already exists.")
        print("--------------------------------------------------")
        return

    student_name = input("Enter Student Name: ")

    student_marks = []

    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))

                if 0 <= mark <= 100:
                    student_marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    avg = sum(student_marks) / len(student_marks)

    student = {
        "id": student_id,
        "name": student_name,
        "marks": student_marks,
        "average": avg
    }

    students.append(student)
    unique_ids.add(student_id)

    print("Student added successfully.")
    print("--------------------------------------------------")


def display_all_students():
    if not students:
        print("No students found.")
        print("--------------------------------------------------")
        return

    print("\nAll Students")
    print("--------------------------------------------------")

    for std in students:
        print(f"""
ID      : {std['id']}
Name    : {std['name']}
Marks   : {std['marks']}
Average : {std['average']:.2f}
""")

    print("--------------------------------------------------")


def search_student():
    student_id = input("Enter Student ID: ")

    for std in students:
        if std["id"] == student_id:
            print("\nStudent Found")
            print("--------------------------------------------------")
            print(f"""
ID      : {std['id']}
Name    : {std['name']}
Marks   : {std['marks']}
Average : {std['average']:.2f}
""")
            print("--------------------------------------------------")
            return

    print("Student not found.")
    print("--------------------------------------------------")


def update_student_marks():
    student_id = input("Enter Student ID: ")

    for std in students:
        if std["id"] == student_id:

            new_marks = []

            for subject in subjects:
                while True:
                    try:
                        mark = int(input(f"Enter new marks for {subject}: "))

                        if 0 <= mark <= 100:
                            new_marks.append(mark)
                            break
                        else:
                            print("Marks should be between 0 and 100.")

                    except ValueError:
                        print("Invalid input. Please enter a number.")

            std["marks"] = new_marks
            std["average"] = sum(new_marks) / len(new_marks)

            print("Student marks updated successfully.")
            print("--------------------------------------------------")
            return

    print("Student not found.")
    print("--------------------------------------------------")


def delete_student():
    student_id = input("Enter Student ID: ")

    for std in students:
        if std["id"] == student_id:
            students.remove(std)
            unique_ids.remove(student_id)

            print("Student deleted successfully.")
            print("--------------------------------------------------")
            return

    print("Student not found.")
    print("--------------------------------------------------")


def top_performing_student():
    if not students:
        print("No students found.")
        print("--------------------------------------------------")
        return

    top_student = max(students, key=lambda student: student["average"])

    print("\nTop Performing Student")
    print("--------------------------------------------------")
    print(f"""
ID      : {top_student['id']}
Name    : {top_student['name']}
Marks   : {top_student['marks']}
Average : {top_student['average']:.2f}
""")
    print("--------------------------------------------------")


# Main Program
while True:
    print("\n===== Student Record Management System =====")
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student By ID")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Display Top Performing Student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_all_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        top_performing_student()

    elif choice == "7":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice. Please try again.")
        print("--------------------------------------------------")