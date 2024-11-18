#!/usr/bin/env python3

# Author ID: yahmad4

class Student:

    # Initialize the student object with name, number, and an empty courses dictionary
    def __init__(self, name, number):
        self.name = str(name)  # Convert name to string
        self.number = str(number)  # Convert number to string
        self.courses = {}  # Dictionary to store course grades

    # Return student name and number as a formatted string
    def displayStudent(self):
        return f'Student Name: {self.name}\nStudent Number: {self.number}'

    # Add a new course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the GPA of the student and handle cases where no courses are present
    def displayGPA(self):
        if not self.courses:  # Check if courses dictionary is empty
            return f'GPA of student {self.name} is 0.0'  # Avoid ZeroDivisionError
        gpa = sum(self.courses.values()) / len(self.courses)  # Calculate GPA
        return f'GPA of student {self.name} is {gpa:.1f}'

    # Return a list of courses the student has passed (grades greater than 0.0)
    def displayCourses(self):
        passed_courses = [course for course, grade in self.courses.items() if grade > 0.0]
        return passed_courses

if __name__ == '__main__':
    # Create first student object and add grades for each class
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades for each class
    student2 = Student('Jessica', 123456)  # Number as integer
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)  # Course not passed

    # Display information for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display information for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
