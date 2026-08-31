# Exercise 1: Define an Empty Vehicle Class
# Problem Statement: Write a Python program to create a
# class named Vehicle that has no variables or methods defined inside it.

class Vehicle:
    pass
print(Vehicle)

# Exercise 2: Vehicle Class with Instance Attributes
# Problem Statement: Write a Python program to create a Vehicle class
# with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.
class Vehicle:
    def __init__(self , name , max_speed , milage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = milage
    
vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")




# Exercise 3: Rectangle Class with Area & Perimeter
# Problem Statement: Write a Python program to create a Rectangle class
# with length and width as instance attributes, and two methods: area()
# that returns the area and perimeter() that returns the perimeter.

class Rectangle:
    def __init__(self, length , width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def parameter(self):
        return 2* (self.length + self.width)
rect = Rectangle(20, 2)
print("Area :" , rect.area())
print("Parameter :" , rect.parameter())

# Exercise 4: Student Class with Average Grade
# Problem Statement: Write a Python program to create a Student class
# that stores a student’s name and a list of marks. Add a 
# method average() that calculates and returns the average of all marks.

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
    def averge(self):
        return sum(self.marks) / len(self.marks)

s1 = Student("Ali" , [30, 40 , 20 ,100, 34])
print(f"{s1.name}'s Average Grade: {s1.averge()}")

# Exercise 5: Product Class with Stock Value Calculator
# Problem Statement: Write a Python program to create a Product class 
# with three instance attributes: name, price, and quantity. Add a method 
# total_value() that returns the total stock value by multiplying price by quantity.

class Product:
    def __init__(self, name, price , quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_value(self):
        return self.price * self.quantity

prdct = Product("Phone" , 100 , 5)
print(f"total stock value of {prdct.name}: {prdct.total_value()} Rs")

# Exercise 6: Bank Account with Deposit & Overdraw Protection
# Problem Statement: Write a Python program to create a BankAccount 
# class with a balance attribute and two methods: deposit(amount) that
# adds funds to the balance, and withdraw(amount) that deducts funds but
# prevents the balance from going below zero.

class BankAccount:
    def __init__(self ,balance):
        self.balance = balance

    def deposit(self , amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self , amount):
        self.balance -= amount
        print(f"Balance after withdrawal: {self.balance}")
        

bnkacnt = BankAccount(1000)
print("balance: " , bnkacnt.balance)
bnkacnt.deposit(200)
print("balance: " , bnkacnt.balance)
bnkacnt.withdraw(300)
print("balance: " , bnkacnt.balance)


# Exercise 7: Light Class with On/Off State Toggle
# Problem Statement: Write a Python program to create a Light class with
# three methods: turn_on() that switches the light on, turn_off() that switches 
# it off, and status() that reports whether the light is currently on or off.

class Light:
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
        print("light is on")

    def turn_Off(self):
        self.is_on = False
        print("light is Off")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")


light = Light()
light.turn_on()
light.status()
light.turn_Off()
light.status()


# Exercise 8: User Class with Password Validation
# Problem Statement: Write a Python program to create a User class 
# that stores a username and a password. Add a check_password(input_password) 
# method that returns True if the input matches the stored password, and False otherwise.
class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
    def checkPassword(self , input_password):
        if(self.password == input_password):
            print("Password Correct")
        else:
            print("password Wrong")
usr = User("Ali" , 123098)
usr.checkPassword(123098)



# Exercise 10: Notebook Class with Add & Display Notes
# Problem Statement: Write a Python program to create a Notebook class 
# that maintains an internal list of notes. Add an add_note(note) method 
# that appends a new note to the list, and a show_notes() method that prints all stored notes.
class Notebook:
    def __init__(self):
        self.notes = []
    def add_note(self ,note):
        self.notes.append(note)
    def show_notes(self):
        for i,note in enumerate(self.notes , start=1):
            print(f"{i}. {note}")
nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_notes()


# Exercise 11: Coffee Machine with Multi-Resource Tracking
# Problem Statement: Write a Python program to create a CoffeeMachine class 
# that tracks three resource attributes: water, coffee, and milk (in ml/g).
# Add a make_latte() method that checks whether sufficient resources are available,
# deducts them if so, and prints an appropriate message in either case.

class CoffeeMachine:
    def __init__(self, water , coffee , milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_lattee(self):
        water_needed = 200
        coffee_needed = 20
        milk_needed = 150

        if self.water > water_needed and self.coffee > coffee_needed and self.milk > milk_needed:
            self.water -= water_needed
            self.coffee -= coffee_needed
            self.milk -= milk_needed
            print(f"Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
        else:
            print("Not enough resources to make a latte.")
machine = CoffeeMachine(water=600, coffee=600, milk=600)
machine.make_lattee()
machine.make_lattee()
machine.make_lattee()

# Exercise 12: Shared Class Attribute Across Instances
# Problem Statement: Write a Python program to create a Vehicle class 
# with a class attribute color = "White" that is shared by all instances.
# Create two vehicle objects and demonstrate that both share the same default color,
# then show that changing the class attribute updates all instances that have not overridden it.

class Vehicle:
    color = "White"
    def __init__(self,name , max_speed):
        self.name = name
        self.max_speed = max_speed

V1 = Vehicle("Tesla" , 250)
V2 = Vehicle("BMW" , 250)

print(f"{V1.name} - Color: {V1.color} - Max-Speed: {V1.max_speed}")
print(f"{V2.name} - Color: {V2.color}, Speed: {V2.max_speed}")

Vehicle.color = "black"

print(f"{V1.name} - Color: {V1.color} - Max-Speed: {V1.max_speed}")
print(f"{V2.name} - Color: {V2.color}, Speed: {V2.max_speed}")

# Exercise 13: Bus Subclass Inheriting from Vehicle
# Problem Statement: Write a Python program to create a Vehicle parent class with 
# name and max_speed attributes and a display() method. Then create a Bus child class 
# that inherits everything from Vehicle without adding anything new, and confirm that 
# an instance of Bus can access the parent’s method.

class Vehicle:
    def __init__(self, name , max_speed):
        self.name = name
        self.max_speed = max_speed

    def display(self):
        print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

class Bus(Vehicle):
    pass

bus1 = Bus("School Bus" , 120)
bus1.display()


# Exercise 14: verride Parent Method Using super()
# Problem Statement: Write a Python program where a Vehicle parent
# class has a seating_capacity() method that accepts a capacity argument.
# Create a Bus child class that overrides this method to provide a default 
# seating capacity of 50, using super() to call the parent’s version internally.

class Vehicle:
    def __init__(self,name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def seating_Capacity(self, capacity):
        print(f"{self.name} seating capacity is: {capacity}")

class Bus(Vehicle):
    def seating_Capacity(self):
        super().seating_Capacity(50)

bus = Bus("School Bus", 120)
bus.seating_Capacity()


# Exercise 15: Add Maintenance Fee in Child Class via super()
# Problem Statement: Write a Python program that creates a Vehicle
# parent class with a base fare, then extends a Taxi child class 
# that adds a 10% maintenance fee on top of the base fare using super().
class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Taxi(Vehicle):
    def __init__(self, base_fare):
        super().__init__(base_fare)
        self.maintenance_fee = base_fare * 0.10

    def total_fare(self):
        return self.base_fare + self.maintenance_fee

taxi = Taxi(500)
print("Total fare with maintenance fee:", taxi.total_fare())



# Exercise 16: Polymorphism with Dog & Cat speak()
# Problem Statement: Write a Python program that defines an Animal base class 
# with a speak() method, then overrides it in Dog and Cat subclasses to return their respective sounds

class Animal:
    def sound(self):
        print("Animal Make some sound")

class Dog(Animal):
    def sound(self):
        print("Wowwwww!")
class Cat(Animal):
    def sound(self):
        print("Meooooo!")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# Exercise 17: Full-Time vs Part-Time Employee Pay Logic
# Problem Statement: Write a Python program that defines an
# Employee base class, then creates FullTimeEmployee and PartTimeEmployee 
# subclasses, each implementing different pay calculation logic.


class Employee:
    def __init__(self, name):
        self.name = name

    def calculatePay(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculatePay(self):
        return self.annual_salary / 12


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculatePay(self):
        return self.hourly_rate * self.hours_worked


ft = FullTimeEmployee("Alice", 60000)
pt = PartTimeEmployee("Bob", 500, 20)

print(f"{ft.name}'s monthly pay: {ft.calculatePay()}")
print(f"{pt.name}'s monthly pay: {pt.calculatePay()}")