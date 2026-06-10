# Week 2 Debugging Project - Bug Report (Version 1)

## Project Name

Student Record Management System (Debugging Edition)

## Objective

Identify, reproduce, document, and resolve bugs present in the Python application.

| Bug ID  | Function            | Bug Type                 | Description                                                                                         | Status |
| ------- | ------------------- | ------------------------ | --------------------------------------------------------------------------------------------------- | ------ |
| BUG-001 | view_students() | Runtime Error | Program tries to access student["score"] but records store "marks". | Fixed |
| BUG-002 | calculate_average() | Logic Error | Average calculation uses len(students)-1, producing incorrect results and possible division errors. | Fixed |
| BUG-003 | search_student() | Logic Error | Search compares original name with lowercase search text incorrectly. | Fixed |
| BUG-004 | save_records() | File Handling Error | File opened in read mode instead of write mode during save operation. | Fixed |
| BUG-005 | load_records() | Exception Handling Error | Program crashes when file does not exist because no exception handling is implemented. | Fixed |
| BUG-006 | add_student()       | Input Validation Error   | Non-numeric marks can crash the application.                                                        | Open   |

## Initial Observation

The application contains multiple issues related to:

* Runtime errors
* Logic errors
* File handling
* Input validation
* Exception handling

These issues will be investigated, reproduced, documented, and resolved during the debugging process.

## Current Status

Bug Analysis Started
Fixes Not Yet Applied



## Debugging Session 2

### Bug ID

BUG-002

### Bug Type

Logic Error

### Function

calculate_average()

### Objective

Verify that average marks are calculated correctly.

### Steps to Reproduce

1. Run the application.
2. Add Student 1 with marks 90.
3. Add Student 2 with marks 97.
4. Select option 3 (Calculate Average).

### Expected Result

Average Marks: 93.5

### Actual Result

Average Marks: 187.0

### Root Cause Analysis

The code divides the total marks using:

len(students) - 1

instead of:

len(students)
1
This causes incorrect average calculations.

### Status

Bug Reproduced

Fix Not Yet Applied

## Debugging Session 3

### Bug ID

BUG-003

### Bug Type

Logic Error

### Function

search_student()

### Objective

Verify that existing students can be searched successfully.

### Steps to Reproduce

1. Run the application.
2. Add a student named Nutan.
3. Select option 4 (Search Student).
4. Enter Nutan as the search value.

### Expected Result

Student Found

Student details should be displayed.

### Actual Result

Student not found

### Root Cause Analysis

The program compares:

student["name"]

with:

search_name.lower()

This converts the search text to lowercase while the stored name remains unchanged.

Example:

Nutan != nutan

As a result, existing students may not be found.

### Status

Bug Reproduced

Fix Not Yet Applied

## Debugging Session 4

### Bug ID

BUG-004

### Bug Type

File Handling Error

### Function

save_records()

### Objective

Verify that student records can be saved successfully.

### Steps to Reproduce

1. Run the application.
2. Add a student record.
3. Select option 5 (Save Records).

### Expected Result

Student records should be written to:

student_data.txt

and a success message should appear.

### Actual Result

The application crashes.

### Error Observed

FileNotFoundError:
No such file or directory: 'student_data.txt'

### Root Cause Analysis

The program attempts to open:

student_data.txt

using read mode ("r").

Read mode requires the file to already exist.

Because the file is missing, Python raises FileNotFoundError before any records can be saved.

### Evidence

Screenshot:
screenshots/bug004_file_handling_error.png

### Status

Bug Reproduced

Fix Not Yet Applied
