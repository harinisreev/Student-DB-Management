import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "students")
    )

# ---------- CREATE ----------
def add_student(name, email, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (name, email, age) VALUES (%s, %s, %s)",
        (name, email, age)
    )
    conn.commit()
    conn.close()
    print(f"[✔] Student '{name}' added successfully!")

def enroll_course(student_id, course_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Courses (course_name, student_id) VALUES (%s, %s)",
        (course_name, student_id)
    )
    conn.commit()
    conn.close()
    print(f"[✔] Student ID {student_id} enrolled in '{course_name}'.")

# ---------- READ ----------
def view_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    conn.close()

    print("\n=== Students ===")
    if rows:
        for r in rows:
            print(f"ID: {r[0]}, Name: {r[1]}, Email: {r[2]}, Age: {r[3]}")
    else:
        print("No students found.")

def view_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Courses")
    rows = cursor.fetchall()
    conn.close()

    print("\n=== Courses ===")
    if rows:
        for r in rows:
            print(f"Course ID: {r[0]}, Name: {r[1]}, Student ID: {r[2]}")
    else:
        print("No courses found.")

def view_student_courses(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT course_id, course_name FROM Courses WHERE student_id = %s",
        (student_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    print(f"\n=== Courses for Student ID {student_id} ===")
    if rows:
        for r in rows:
            print(f"Course ID: {r[0]}, Name: {r[1]}")
    else:
        print("No courses found for this student.")

# ---------- UPDATE ----------
def update_student(student_id, new_email=None, new_age=None):
    conn = get_connection()
    cursor = conn.cursor()

    if new_email:
        cursor.execute(
            "UPDATE Students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )
    if new_age:
        cursor.execute(
            "UPDATE Students SET age = %s WHERE student_id = %s",
            (new_age, student_id)
        )

    conn.commit()
    conn.close()
    print(f"[✔] Student ID {student_id} updated successfully!")

def update_course(student_id, old_course, new_course):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Courses SET course_name = %s WHERE student_id = %s AND course_name = %s",
        (new_course, student_id, old_course)
    )
    conn.commit()
    conn.close()
    print(f"[✔] Course updated for Student ID {student_id}.")

# ---------- DELETE ----------
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Courses WHERE student_id = %s", (student_id,))
    cursor.execute("DELETE FROM Students WHERE student_id = %s", (student_id,))
    conn.commit()
    conn.close()
    print(f"[✔] Student ID {student_id} and their courses deleted.")

def delete_course(student_id, course_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Courses WHERE student_id = %s AND course_name = %s",
        (student_id, course_name)
    )
    conn.commit()
    conn.close()
    print(f"[✔] Course '{course_name}' removed for Student ID {student_id}.")

# ---------- MENU ----------
def menu():
    while True:
        print("\n=== Student Course Management System ===")
        print("1. Add Student")
        print("2. Enroll in Course")
        print("3. View All Students")
        print("4. View All Courses")
        print("5. View Courses by Student")
        print("6. Update Student")
        print("7. Update Course")
        print("8. Delete Student")
        print("9. Delete Course")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            add_student(name, email, age)

        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            course_name = input("Enter course name: ")
            enroll_course(student_id, course_name)

        elif choice == "3":
            view_all_students()

        elif choice == "4":
            view_all_courses()

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            view_student_courses(student_id)

        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            new_email = input("Enter new email (or leave blank): ")
            new_age_input = input("Enter new age (or leave blank): ")
            new_age = int(new_age_input) if new_age_input else None
            update_student(student_id, new_email if new_email else None, new_age)

        elif choice == "7":
            student_id = int(input("Enter student ID: "))
            old_course = input("Enter old course name: ")
            new_course = input("Enter new course name: ")
            update_course(student_id, old_course, new_course)

        elif choice == "8":
            student_id = int(input("Enter student ID: "))
            delete_student(student_id)

        elif choice == "9":
            student_id = int(input("Enter student ID: "))
            course_name = input("Enter course name: ")
            delete_course(student_id, course_name)

        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice. Try again.")

# ---------- Run Program ----------
if __name__ == "__main__":
    menu()
