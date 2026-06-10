# Python Utility Toolkit with Automated Testing

## Overview

This project is a Python-based utility toolkit developed to demonstrate automated software testing using the Pytest framework. The project contains multiple utility modules for mathematical calculations, string manipulation, and file handling operations.

The main goal of this project is to apply software testing concepts such as unit testing, edge case validation, exception handling, and Test-Driven Development (TDD) practices to ensure application reliability and maintainability.

---

## Features

### Calculator Module

* Addition
* Subtraction
* Multiplication
* Division
* Division by zero exception handling

### String Utility Module

* Reverse string
* Count vowels
* Palindrome checking

### File Handler Module

* Write content to file
* Read content from file

---

## Automated Testing

Automated tests are implemented using the `pytest` framework.

### Test Coverage Includes:

* Functional testing
* Unit testing
* Edge case testing
* Exception handling
* File operation testing

---

## Project Structure

```bash
python-testing-project/
│
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── string_utils.py
│   └── file_handler.py
│
├── tests/
│   ├── test_calculator.py
│   ├── test_string_utils.py
│   └── test_file_handler.py
│
├── README.md
├── requirements.txt
└── run.py
```

---

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python run.py
```

---

## Run Automated Tests

```bash
python -m pytest
```

---

## Technologies Used

* Python
* Pytest
* Git & GitHub
* VS Code

---

## Output

All automated tests successfully passed.

```bash
10 passed
```

---

## Conclusion

This project demonstrates the practical implementation of automated testing in Python applications. The use of Pytest improves software reliability, maintainability, and debugging efficiency while following clean coding and testing practices.
