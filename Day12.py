# ---------->Assignment 1
# Create a class:
# class Car
# Store:
# brand
# model
# Create one object and print both values.

class car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model;


car1 = car("Mercedise" , 1999)
print(car1.model)
print(car1.brand)



# --------->Assignment 2
# Create:
# class Student
# Store:
# name
# semester
# Create your own object and print both values.

class Student:
    def __init__(self , name , semester):
        self.name = name
        self.semester = semester

Student1 = Student("Ali" , 6)
print(Student1.name)
print(Student1.semester)


# ----------->Assignment 3
# Create a method:
# greet()
# that prints:
# Hello Abdul Haseeb

class boy:
    def __init__(self , name):
        self.name = name
        
    def greet(self):
        print("Hello" , self.name)

boy1 = boy("Abdul Haseeb")
boy1.greet()