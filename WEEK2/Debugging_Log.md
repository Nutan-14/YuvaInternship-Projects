# Week 2 Debugging Log

## Project Name

Student Record Management System (Debugging Edition)

## Debugging Session 1

### Bug ID

BUG-001

### Bug Type

Runtime Error

### Function

view_students()

### Objective

Verify that student records can be displayed correctly.

### Steps to Reproduce

1. Run the application.
2. Select option 1 (Add Student).
3. Enter a student name.
4. Enter marks.
5. Select option 2 (View Students).

### Expected Result

The application should display:

Name: Student Name

Marks: Student Marks

### Actual Result

The application crashes while displaying student records.

### Error Observed

KeyError: 'score'

### Root Cause Analysis

Student records are stored using the key:

"marks"

However, the code attempts to access:

student["score"]

Since the key "score" does not exist inside the dictionary, Python raises a KeyError.

### Evidence

Screenshot:
screenshots/bug001_runtime_error.png

### Status

Bug Reproduced

Fix Not Yet Applied
