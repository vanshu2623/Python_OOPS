# Task 1
class Student:   # Student class creation

    # Constructor to initialize the value of the class
    def __init__(self,name,rollno,course,email):
        self.name = name
        self.rollno = rollno
        self.course = course
        self.email = email
    
    def display_student(self):          # Method to display the value of the class
            if "Python".lower() in self.course:
                print(f"Python Based Courses:",self.course)
                
            print("Name:",self.name,"\nRollNo:",self.rollno,"\nCourse:",self.course,"\nEmail:",self.email) 

s1 = Student("Vanshika",101,"Python Full Stack","vanshika@gmail.com")        # Creating an object of Student class
s2 = Student("Neha",102,"Python Full Stack","neha@gmail.com")
s3 = Student("Komal",103,"Java Full Stack","komal@gmail.com")
s1.display_student()  
print("--"*15)       # Print a blank line for better readability
s2.display_student()

students_list = [s1,s2,s3]

for stud_obj in students_list:

    if "Python".lower() in stud_obj.course.lower():
        print(stud_obj.name)

s1.display_student()
s2.display_student()
s3.display_student()


