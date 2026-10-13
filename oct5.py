# Base , Super , Parent Class
class A:
    p = 20

    def m1(self):
        print("This is method m1 of class A")

    def m2(self):
        print("This is method m2 of class A")   

# Derived , Sub , Child Class
class B(A):
    q = 30

    def m3(self):
        print("This is method m3 of class B")

    def m4(self):
        print("This is method m4 of class B")            


obj2 = B()

obj2.m1()
obj2.m2()
obj2.m3()
obj2.m4()

class A:
    p = 20

    def m1(self):
        print("This is method m1 of class A")
        return 11111

    def m2(self):
        print("This is method m2 of class A")  
        s = "Vanshika" 
        s.upper()
        return s

class B(A):
    q = 30

    def m3(self):
        print("This is method m3 of class B")
        l = [20,30,40,10]
        return l

    def m4(self):
        print("This is method m4 of class B")
        d = {"name":"Vanshika","age":23} 
        return d

obj2 = B()    

print(obj2.m1())
print(obj2.m2())
print(obj2.m3())
print(obj2.m4())