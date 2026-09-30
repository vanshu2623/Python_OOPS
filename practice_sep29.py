# Task 5

class Address: 
    def __init__(self, city, pincode): 
        self.city = city 
        self.pincode = pincode 
 
 
class Student: 
    def __init__(self, roll, name, marks, address): 
        self.roll = roll 
        self.name = name 
        self.marks = marks 
        self.address = address 
 
 
class Teacher: 
    def __init__(self, name, salary, department, address): 
        self.name = name 
        self.salary = salary 
        self.department = department 
        self.address = address 
 
 
class College: 
    def __init__(self, students, teachers): 
        self.students = students 
        self.teachers = teachers 
 
 
a1 = Address("Nagpur", 440001) 
a2 = Address("Pune", 411001) 
 
s1 = Student(101, "Vanshika", 85, a1) 
 
t1 = Teacher("Rahul", 50000, "Computer Science", a2) 
 
c1 = College(s1, t1) 
 
print("Student Details:") 
print(c1.students.roll) 
print(c1.students.name) 
print(c1.students.marks) 
print(c1.students.address.city) 
print(c1.students.address.pincode) 
 
print("\nTeacher Details:") 
print(c1.teachers.name) 
print(c1.teachers.salary) 
print(c1.teachers.department) 
print(c1.teachers.address.city) 
print(c1.teachers.address.pincode)