class Book:
    def __init__(self,t,p):
        self.title = t
        self.price = p
    def __add__(self,other):
        # return self.price * other.price
        # return self.price + other.price 
        return self.title + other.title 

b1 = Book("Core Python",200)
b2 = Book("Advanced Python",600)

print(b1 + b2)

class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p

    def __add__(self, other):
        return Book(self.title + " " + other.title,
                    self.price + other.price)


b1 = Book("Core Python", 200)
b2 = Book("Advanced Python", 600)
b3 = Book("Java Programming", 500)

b4 = b1 + b2 + b3

print(b4.title)
print(b4.price)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee("", self.salary + other.salary)


e1 = Employee("Amit", 25000)
e2 = Employee("Rahul", 30000)
e3 = Employee("Neha", 35000)

e4 = e1 + e2 + e3

print(e4.salary)

class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p

    def __mul__(self, other):
        return self.price * other.price

    def __truediv__(self, other):
        return self.price / other.price


b1 = Book("Core Python", 200)
b2 = Book("Advanced Python", 4)

print(b1 * b2)
print(b1 / b2)