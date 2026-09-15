# Student Management System
# Skillnexis Week 2 Project

import csv

FILE_NAME = "students.csv"


# -------------------------
# ADD STUDENT
# -------------------------

def add_student():
    try:
        roll_number = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll_number, name, marks])

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid marks.")


# -------------------------
# VIEW STUDENTS
# -------------------------

def view_students():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            print("\n====================================")
            print("          STUDENT RECORDS")
            print("====================================")

            found = False

            for row in reader:
                if row:
                    found = True
                    print(
                        "Roll Number:", row[0],
                        "| Name:", row[1],
                        "| Marks:", row[2]
                    )

            if not found:
                print("No student records found.")

    except FileNotFoundError:
        print("Student file not found.")


# -------------------------
# SEARCH STUDENT
# -------------------------

def search_student():
    roll_number = input("Enter Roll Number to search: ")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0] == roll_number:
                    print("\nStudent Found!")
                    print("Roll Number:", row[0])
                    print("Name:", row[1])
                    print("Marks:", row[2])
                    return

        print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")


# -------------------------
# DELETE STUDENT
# -------------------------

def delete_student():
    roll_number = input("Enter Roll Number to delete: ")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            rows = list(csv.reader(file))

        found = False

        for row in rows:
            if row and row[0] == roll_number:
                rows.remove(row)
                found = True
                break

        if found:
            with open(FILE_NAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Student deleted successfully!")

        else:
            print("Student not found.")

    except FileNotFoundError:
        print("Student file not found.")


# -------------------------
# MAIN MENU
# -------------------------

print("====================================")
print("     STUDENT MANAGEMENT SYSTEM")
print("====================================")

while True:

    print("\n------------ MENU ------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")