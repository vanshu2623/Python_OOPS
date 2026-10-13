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

