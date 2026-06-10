students = []


def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students.append({
        "name": name,
        "marks": marks
    })

    print("Student added successfully")


def view_students():
    print("\nStudent Records")

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["score"])   # BUG


def calculate_average():
    total = 0

    for student in students:
        total += student["marks"]

    average = total / (len(students) - 1)   # BUG

    print("Average Marks:", average)


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"] == search_name.lower():   # BUG
            print("Student Found")
            print(student)
            found = True

    if found == False:
        print("Student not found")


def save_records():
    file = open("student_data.txt", "r")   # BUG

    for student in students:
        file.write(
            student["name"] +
            "," +
            str(student["marks"]) +
            "\n"
        )

    file.close()

    print("Records saved successfully")


def load_records():
    file = open("student_data.txt", "r")

    data = file.readlines()

    for line in data:
        parts = line.strip().split(",")

        students.append({
            "name": parts[0],
            "marks": int(parts[1])
        })

    print("Records loaded successfully")


while True:

    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Average")
    print("4. Search Student")
    print("5. Save Records")
    print("6. Load Records")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        calculate_average()

    elif choice == "4":
        search_student()

    elif choice == "5":
        save_records()

    elif choice == "6":
        load_records()

    elif choice == "7":
        print("Thank you")
        break

    else:
        print("Invalid choice")