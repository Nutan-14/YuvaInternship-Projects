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


# Slow function to calculate average marks
def calculate_average_marks(students):

    total = 0

    # Unnecessary nested loop (intentionally slow)
    for student in students:
        for i in range(1):
            total += student["marks"]

    average = total / len(students)

    return average


# Slow search function
def find_student_by_id(students, student_id):

    # Linear search (slow for large data)
    for student in students:
        if student["id"] == student_id:
            return student

    return None


# Slow function to find top student
def find_top_student(students):

    top_student = students[0]

    for student in students:
        time.sleep(0.0001)  # Intentional delay

        if student["marks"] > top_student["marks"]:
            top_student = student

    return top_student


# Slow sorting function
def sort_students_by_marks(students):

    # Bubble sort (intentionally slow)
    n = len(students)

    for i in range(n):
        for j in range(0, n - i - 1):

            if students[j]["marks"] > students[j + 1]["marks"]:

                temp = students[j]
                students[j] = students[j + 1]
                students[j + 1] = temp

    return students


# Main program
def main():
    start_time = time.time()

    print("Generating student records...")

    students = generate_students(5000)

    print("Calculating average marks...")
    average = calculate_average_marks(students)

    print("Finding a student...")
    student = find_student_by_id(students, 4500)

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