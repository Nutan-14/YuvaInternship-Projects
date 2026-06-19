# Security Audit Report

## Project Name

Secure Notes Management System

## Objective

The objective of this project was to identify security vulnerabilities in a Python application and implement secure coding practices to protect user data and improve application security.

## Vulnerabilities Identified

### 1. Weak Username Validation

**Issue:**
The application accepted invalid usernames.

**Risk:**
Invalid and inconsistent user data could be stored.

**Fix Applied:**
Implemented username length validation with a minimum length of 3 characters.

---

### 2. Weak Password Acceptance

**Issue:**
Users could create weak passwords.

**Risk:**
Weak passwords are easier to guess and compromise.

**Fix Applied:**
Implemented password strength validation requiring:

* Minimum 8 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one number

---

### 3. Plain Text Password Storage

**Issue:**
Passwords could be stored in readable format.

**Risk:**
Exposure of user credentials if storage files are accessed.

**Fix Applied:**
Implemented SHA-256 password hashing using Python's hashlib module before storing passwords.
