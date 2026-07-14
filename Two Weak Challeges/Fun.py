# Exercise 1. Create a Function with Parameters
# Practice Problem: Write a function called demo() that
# accepts two parameters: a name and an age. The function 
# should print these values directly to the console.

def demo(name , age):
    print(f"Name = {name} and Age = {age}")

demo("Abdul Haseeb" , 22)


# Exercise 2. Variable Length of Arguments (*args)
# Practice Problem: Create a function func1() such that it 
# can accept a variable number of arguments and print all of them.
# Whether you pass two numbers or five, the function should handle them all without error

def funct1(*args):
    print("Printing values:")
    for i in args:
        print(i)


funct1(20, 40, 60)


# Exercise 3. Return Multiple Values from a Function
# Practice Problem: Write a function calculation() that accepts
# two variables and calculates both addition and subtraction. 
# The function must return both results in a single return statement.

def Calculation(var1 , var2):
    Addition = var1 + var2
    Multiplication = var1 * var2
    return Addition , Multiplication


res = (Calculation(3, 4))
print(res)


# Exercise 4. Function with Default Argument
# Practice Problem: Create a function show_employee() that accepts 
# an employee’s name and salary. If the salary is not provided in the
# function call, the function should automatically assign a default value of 9000.

def show_employee(name , sallary=10000):
    print("Name: ",  name , "Sallary: ", sallary)

show_employee("Ali")



# Exercise 5. Create an Inner Function
# Practice Problem: Create an outer function that accepts two
# parameters, a and b. Inside, create an inner function that 
# calculates the addition of a and b. The outer function should
# then add 5 to that sum and return the final result.

def outer(a , b):
    def inner(a, b):
        return a + b
    add = inner(a,b)
    return add +5

result = outer(5, 10)
print(result)


# Exercise 6. Create a Recursive Function
# Practice Problem: Write a recursive function addition() 
# that calculates the sum of numbers from 0 to 10. A recursive function
# is a function that calls itself to solve smaller instances of the same problem.
def addition(num):
    if(num):
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)


# Exercise 7. Assign a Different Name to Function and Call It
# Practice Problem: Assign a different name to the function display_student(name, age)
# and call it using the new name. For example, assign it to a variable called show_student.

def display_student(name , age):
    print("Name: ",name , "Age: :", age)

show_students = display_student

show_students("Ali" , 19)



# Exercise 8. Generate a List of Even Numbers (Range Function)
# Practice Problem: Create a function that generates a list of all even numbers between 4 and 30.
def Even_Num():
    return list(range(4,30,2))

print(Even_Num())



# Exercise 9. Find the Largest Item in a List
# Practice Problem: Create a function that takes a list of numbers 
# as input and returns the largest item from that list without using the
# built-in max() function (to practice manual logic).

def find_largest(list_input):
    largest = list_input[0]

    for num in list_input:
        if num > largest:
            largest = num
    return largest
    
x = [4,6,7,3,5,6,74]
print(find_largest(x))

student = {"name": "Alice", "age": 20, "grade": "B"}

# Add a new key
print("Name:", student["name"])
