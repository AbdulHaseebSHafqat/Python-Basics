# Exercise 1. Accept numbers from a user
# Practice Problem: Write a program that accepts two integer numbers
# from the user and calculates their multiplication. Print the final result to the console.
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
print("The Multiplcation is: ",number1 * number2 )


# Exercise 2. Display variables with a separator
# Practice Problem: Use the print() function to format the
# words “Name”, “Is”, and “James” so they appear with three asterisks (***) between them.

print("Name", "Is" , "James" , sep="***")

# Exercise 3. Convert decimal number to octal
# Practice Problem: Accept an integer from the user 
# and display it as an octal number (Base 8).

num = 10
print(oct(num))

# Exercise 4. Binary representation
# Practice Problem: Accept an integer from the user 
# and display its value in binary format (Base 2).

number = int(input("Enter a number: "))
print(bin(number))

# Exercise 5. Accept any three strings from one input() call
# Practice Problem: Write a program that takes three names (or any words)
# from a user in a single input prompt and assigns them to three separate variables.

name1 , name2 , name3 = input("Enter your name: ").split()
print(name1)
print(name2)
print(name3)

# Exercise 6. Hexadecimal representation
# Practice Problem: Accept an integer and display its value in hexadecimal format (Base 16).

num = int(input("Enter the number"))
print(hex(num))

# Exercise 7. Display float number with 2 decimal places"
# Practice Problem: Display a float number (a number with decimals)
# such as 458.541315 rounded to exactly two decimal places.

number = 123.4344
print(f"{number:.2f}")


# Exercise 8. Percentage display
# Practice Problem: Ask the user for a numerator and a denominator.
# Calculate the percentage (numerator/denominator * 100) and display
# it with exactly two decimal places followed by a percent sign.

numerator = int(input("Enter the numerator number:"))
denominator = int(input("Enter the denominator number: "))
percenatage = (numerator/denominator)*100
print(f"{percenatage:.2f}%")

# Exercise 9: Display right-aligned output
# Practice Problem: Ask the user for a word and a number.
# Print the word right-aligned in a total field width of 20 characters, followed by the number.

Word = "Python"
space = 20
print(f"{Word:>20}")

# imp
# f"{title:-<40}"   # Left
# f"{title:->40}"   # Right
# f"{title:-^40}"   # Center

# Exercise 10. Center-aligned text
# Practice Problem: Display a string centered within a 40-character field, 
# using hyphens (-) as the padding character.
string = "Abdul Haseeb"
print(f"{string:-^40}")


# Exercise 11: Padding with zeros
# Practice Problem: Ask the user for a number.
# Print this number padded with leading zeros so the total width is exactly 5 digits

number = input("Enter a number")
print(number.zfill(5))

# Exercise 12: Format variables using string.format() method
# Practice Problem: Given three variables quantity = 3, totalMoney = 450,
# and price = 150, use the format() method to print a sentence that neatly displays these values.

quantity = 3
totalMoney = 450
price = 150
statement = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."

print(statement.format(quantity, totalMoney, price))


# Exercise 14: Accept a list of 5 float numbers
# Practice Problem: Write a program that accepts 5 float numbers as input 
# from the user and stores them in a list.

numbers = []
for i in range(0 ,5):
    print("Enter number at location", i, ":")
    item = float(input())
    numbers.append(item)

print("User List:", numbers)


# Exercise 15. Tabular output from lists
# Practice Problem: You have two lists: names = ["Alice", "Bob", "Charlie"]
# and scores = [85, 92, 78]. Print these as a table with aligned columns.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score'}")
print("-" * 15)

for name, score in zip(names, scores):
    print(f"{name:<10} {score}")


# Exercise 16. Interactive menu
# Practice Problem: Create a menu that offers three options:
# “1. Say Hello”, “2. Calculate Square”, and “3. Exit”.
# The program should perform the action based on the number the user types.




print("1. Say Hello\n2. Calculate Square\n3. Exit")
choice = input("Enter choice (1-3): ")
if choice == "1":
    print("Hello there! Hope you're having a great day.")
elif choice == '2':
    val = int(input("Enter a number to calculate square: "))
    print(f"The square is: {val * val}")
elif choice == 3:
    print("Exiting... Goodbye!")
else:
    print("Invalid choice. Please pick 1, 2, or 3.")


# Exercise 17. Masked password input (getpass)
# Practice Problem: Write a script that asks a user for their username 
# using standard input and their password using masked input 
# (where the characters don’t appear on the screen).

import getpass
user = input("Enter username")
pwd = getpass.getpass("Password")

if (user == "Admin" and pwd == "SecretPasswrod123"):
    print(f"Login successful for {user}!")
else:
    print("Access Denied.")
# :
# this is used for tell that after that we start formating like use formula