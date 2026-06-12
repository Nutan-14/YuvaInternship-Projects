import random
import time


# Function to generate student records
def generate_students(num_students):

    students = []

    for i in range(num_students):

        student = {
            "id": i,
            "name": "Student_" + str(i),
            "marks": random.randint(40, 100)
        }

        students.append(student)

    return students


# Optimized average calculation
def calculate_average_marks(students):

    total = sum(student["marks"] for student in students)

    average = total / len(students)

    return average


# Optimized search using dictionary
def create_student_lookup(students):

    student_lookup = {}

    for student in students:
        student_lookup[student["id"]] = student

    return student_lookup


def find_student_by_id(student_lookup, student_id):

    return student_lookup.get(student_id, None)


# Optimized top student finder
def find_top_student(students):

    top_student = max(students, key=lambda student: student["marks"])

    return top_student


# Optimized sorting
def sort_students_by_marks(students):

    sorted_students = sorted(students, key=lambda student: student["marks"])

    return sorted_students


# Main program
def main():

    start_time = time.time()

    print("Generating student records...")

    students = generate_students(5000)

    print("Creating student lookup dictionary...")
    student_lookup = create_student_lookup(students)

    print("Calculating average marks...")
    average = calculate_average_marks(students)

    print("Finding a student...")
    student = find_student_by_id(student_lookup, 4500)

    print("Finding top student...")
    top_student = find_top_student(students)

    print("Sorting students...")
    sorted_students = sort_students_by_marks(students)

    print("\n----- RESULTS -----")
    print("Average Marks:", average)
    print("Found Student:", student)
    print("Top Student:", top_student)
    print("Total Sorted Students:", len(sorted_students))

    end_time = time.time()

    execution_time = end_time - start_time

    print("\nExecution Time:", execution_time, "seconds")


# Run program
main()