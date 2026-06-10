students = []


def add_student():

    name = input("Enter student name: ")

    try:
        marks = int(input("Enter marks: "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100")
            return

    except ValueError:
        print("Invalid marks. Please enter numbers only.")
        return

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully")


def view_students():

    if len(students) == 0:
        print("No student records found")
        return

    print("\n===== Student Records =====")

    for student in students:
        print("-------------------------")
        print("Name :", student["name"])
        print("Marks:", student["marks"])

    print("-------------------------")

def calculate_average():
    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", average)


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("Student Found")
            print(student)
            found = True

    if found == False:
        print("Student not found")


def save_records():
    file = open("student_data.txt", "w")

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
    try:
        students.clear()
        file = open("student_data.txt", "r")

        data = file.readlines()

        for line in data:
            parts = line.strip().split(",")

            students.append({
                "name": parts[0],
                "marks": int(parts[1])
            })

        file.close()

        print("Records loaded successfully")

    except FileNotFoundError:
        print("No saved records found.")


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