Student Record Management System (Python + MySQL)

Author: Harinisree Venkatesan

Overview

A Command-Line Interface (CLI) application to manage students and their course enrollments using Python and MySQL. Supports CRUD operations:
Create: Add students & enroll in courses
Read: View students & courses
Update: Modify student or course details
Delete: Remove students or courses

The CLI provides user-friendly navigation for all operations.

How It Works:

Run the program → menu appears
Choose an option → enter required inputs
SQL query executes → changes saved (conn.commit())
Results displayed → loop continues until exit

Example:

Enter name: John Doe
Enter email: john@example.com
Enter age: 22
Message: Student added successfully.

CLI Menu Options:

Add Student
Enroll in Course
View Students
Update Student/Course
Delete Student/Course
Exit


Tech Stack:

Python 3
MySQL

MySQL Connector for Python

Groq LLM API (for agent ideas)
