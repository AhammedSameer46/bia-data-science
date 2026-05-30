# Student Management System

students = []
subjects = ("Math", "Science", "English")
course_names = set()


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    course_names.add(course)

    print("Student added successfully!")


def display_students():
    if not students:
        print("No students found.")
        return

    print("\n----- STUDENT LIST -----")

    for index, student in enumerate(students, start=1):
        result = "Pass" if student["marks"] >= 50 else "Fail"

        print(f"\nStudent {index}")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
        print(f"Result: {result}")


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            print(student)
            return

    print("Student not found.")


def update_marks():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            new_marks = float(input("Enter New Marks: "))
            student["marks"] = new_marks
            print("Marks updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def highest_mark():
    if not students:
        print("No student data available.")
        return

    highest = max(students, key=lambda s: s["marks"])

    print("\nHighest Scorer")
    print("Name:", highest["name"])
    print("Marks:", highest["marks"])


def average_mark():
    if not students:
        print("No student data available.")
        return

    total = sum(student["marks"] for student in students)
    avg = total / len(students)

    print("Average Mark:", round(avg, 2))


def save_to_file():
    with open("students.txt", "w") as file:
        for student in students:
            line = (
                f"{student['id']},"
                f"{student['name']},"
                f"{student['age']},"
                f"{student['course']},"
                f"{student['marks']}\n"
            )
            file.write(line)

    print("Data saved successfully.")


def load_from_file():
    try:
        with open("students.txt", "r") as file:
            students.clear()

            for line in file:
                data = line.strip().split(",")

                student = {
                    "id": data[0],
                    "name": data[1],
                    "age": int(data[2]),
                    "course": data[3],
                    "marks": float(data[4])
                }

                students.append(student)
                course_names.add(data[3])

        print("Data loaded successfully.")

    except FileNotFoundError:
        print("students.txt not found.")


def display_courses():
    print("Unique Courses:")
    print(course_names)


def display_subjects():
    print("Subjects:")
    print(subjects)


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Highest Mark")
    print("7. Average Mark")
    print("8. Save to File")
    print("9. Load from File")
    print("10. Display Courses")
    print("11. Display Subjects")
    print("12. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        highest_mark()

    elif choice == "7":
        average_mark()

    elif choice == "8":
        save_to_file()

    elif choice == "9":
        load_from_file()

    elif choice == "10":
        display_courses()

    elif choice == "11":
        display_subjects()

    elif choice == "12":
        print("Exiting application...")
        break

    else:
        print("Invalid choice.")