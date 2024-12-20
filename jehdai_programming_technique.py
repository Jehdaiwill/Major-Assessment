# -*- coding: utf-8 -*-
"""Jehdai Programming Technique

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ozF-EzMA7hBhy66qrdn1wrlfSUBVOqzq
"""

# Course class: Is a course with an ID, name, and fee.
class Course:
    def __init__(self, course_id, name, fee):
        # Initialize course with ID, name, and fee.
        self.course_id = course_id
        self.name = name
        self.fee = fee

    def __str__(self):
        # Print the course details.
        return f"{self.name} (ID: {self.course_id}) - Fee: ${self.fee}"

# Student class: Represents a student with an ID, name, email, and balance.
class Student:
    def __init__(self, student_id, name, email):
        # Initialize student with ID, name, email, and empty course list.
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []  # List of courses the student is enrolled in.
        self.balance = 0   # Total balance for all enrolled courses.

    def enroll(self, course):
        # Enroll student in a course and add the course fee to the balance.
        if course not in self.courses:
            self.courses.append(course)
            self.balance += course.fee  # Add course fee to student's balance.

    def __str__(self):
        # Print student details including balance.
        return f"Student {self.name} (ID: {self.student_id}) - Balance: ${self.balance}"

# Registration System class: Manages courses and students.
class RegistrationSystem:
    def __init__(self):
        # Initialize empty course list and student dictionary.
        self.courses = []
        self.students = {}

    def add_course(self, course_id, name, fee):
        # Add a new course if it doesn't exist already.
        for course in self.courses:
            if course.course_id == course_id:
                return  # Don't add the course again if it already exists.
        new_course = Course(course_id, name, fee)
        self.courses.append(new_course)

    def register_student(self, student_id, name, email):
        # Register a new student if they don't exist already.
        if student_id not in self.students:
            new_student = Student(student_id, name, email)
            self.students[student_id] = new_student

    def enroll_student_in_course(self, student_id, course_id):
        # Enroll a student in a course.
        student = self.students.get(student_id)
        if not student:
            return "Student not found."

        course = None
        for c in self.courses:
            if c.course_id == course_id:
                course = c
                break

        if not course:
            return "Course not found."

        student.enroll(course)
        return f"{student.name} successfully enrolled in {course.name}."

    def make_payment(self, student_id, amount):
        # Make a payment and update the student's balance.
        student = self.students.get(student_id)
        if not student:
            return "Student not found."

        if amount < 0.4 * student.balance:
            return "Minimum payment is 40% of the balance."

        student.balance -= amount
        return f"Payment successful! New balance: ${student.balance}"

    def show_courses(self):
        # Show all available courses.
        for course in self.courses:
            print(course)

    def show_students(self):
        # Show all registered students.
        for student in self.students.values():
            print(student)

    def show_students_in_course(self, course_id):
        # Show students enrolled in a specific course.
        course = None
        for c in self.courses:
            if c.course_id == course_id:
                course = c
                break

        if not course:
            return " Course not found."

        enrolled_students = [student for student in self.students.values() if course in student.courses]
        if not enrolled_students:
            return "There are no students that are enrolled in this course."

        for student in enrolled_students:
            print(student)

# Now create the registration system and perform some actions.
if __name__ == "__main__":
    # Initialize the system.
    system = RegistrationSystem()

    # Add courses.
    system.add_course(101, "Intro to Life Science", 100)
    system.add_course(102, "Kinetic Studies 12", 150)

    # Register students.
    system.register_student(1, "Jehdai", "jehdai@ucc.com")
    system.register_student(2, "Sharon", "sharon@ucc.com")

    # Enroll students in courses.
    print(system.enroll_student_in_course(1, 101))  # Jehdai enrolls in Intro to Life Science
    print(system.enroll_student_in_course(2, 101))  # Sharon enrolls in Intro to Life Science
    print(system.enroll_student_in_course(2, 102))  # Sharon enrolls in Kinetic Studies 12

    # Show available courses.
    print("\nAvailable Courses:")
    system.show_courses()

    # Show all students.
    print("\nRegistered Students:")
    system.show_students()

    # Show students in a specific course.
    print("\nStudents in 'Intro to Life Science' (Course ID: 101):")
    system.show_students_in_course(101)

    # Make a payment for a student.
    print("\nJehdai's Payment:")
    print(system.make_payment(1, 40))  # Jehdai has a payment of $40

    # Show updated balance after payment.
    print("\nUpdated Balance for Jehdai:")
    system.show_students()