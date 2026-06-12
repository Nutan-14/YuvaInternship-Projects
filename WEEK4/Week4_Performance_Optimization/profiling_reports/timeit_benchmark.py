import timeit


# Benchmark original version
original_time = timeit.timeit(
    stmt="""
students = []

for i in range(5000):
    students.append({
        "id": i,
        "name": "Student_" + str(i),
        "marks": i % 100
    })

# Bubble sort
n = len(students)

for i in range(n):
    for j in range(0, n - i - 1):

        if students[j]["marks"] > students[j + 1]["marks"]:

            temp = students[j]
            students[j] = students[j + 1]
            students[j + 1] = temp
""",
    number=1
)


# Benchmark optimized version
optimized_time = timeit.timeit(
    stmt="""
students = []

for i in range(5000):
    students.append({
        "id": i,
        "name": "Student_" + str(i),
        "marks": i % 100
    })

sorted_students = sorted(
    students,
    key=lambda student: student["marks"]
)
""",
    number=1
)


print("Original Version Time:", original_time, "seconds")

print("Optimized Version Time:", optimized_time, "seconds")