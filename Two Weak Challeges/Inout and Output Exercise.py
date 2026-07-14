# # --------------->Problem1
# Write a program that accepts two integer numbers from the user
# and calculates their multiplication. Print the final result to the console
number1 = int(input("Enter 1st number: "))
number2 = int(input("Enter 2nd number: "))
multiplication = number1 * number2
print("Final Result", multiplication)

# --------------->Problem2
# Use the print() function to format the words 
# “Name”, “Is”, and “James” so they appear with three asterisks (***) between them.

print("Name" , "Is" , "James", sep="***")


# --------------->Problem3
#  Write a program that takes three names (or any words) from 
# a user in a single input prompt and assigns them to three separate variables.

name1 , name2 , name3 = input("Enter your name").split()
print("name1: ", name1)
print("name2: ", name2)
print("name3: ", name3)

# --------------->Problem8
# Practice Problem: Ask the user for a numerator and a denominator. 
# Calculate the percentage (numerator/denominator * 100) and display it with exactly two decimal places followed by a percent sign.

numerator = int(input("Enter a numerator"))
denominatior = int(input("Enter a denominator"))

percentage = (numerator / denominatior) * 100

print(f"The result is : {percentage:.2f}")


# --------------->Problem7
# Display a float number (a number with decimals)
# such as 458.541315 rounded to exactly two decimal places.

number = 29.343423
print(f"{number:.2f}")
print("%.2f" % number)


# --------------->Problem9
# Ask the user for a word and a number.
#  Print the word right-aligned in a total field width of 20 characters, followed by the number.
word = input("Enter a word: ")
version = input("Enter a version number: ")

# Right-align the word in 20 spaces
print(f"{word:>100} {version}")


title = "Report Summary"
formated_title = print(f"{title:-<40}")








# imp:
# Use of "Sep" Keyword
# Use the print() function to format the words 
# “Name”, “Is”, and “James” so they appear with three asterisks (***) between them.

# print("Name" , "Is" , "James", sep="***")


#  Use of "split" Keyword
#  Write a program that takes three names (or any words) from 
# a user in a single input prompt and assigns them to three separate variables.

# name1 , name2 , name3 = input("Enter your name").split()


#  Use of ".2f" Keyword
# Display a float number (a number with decimals)
# such as 458.541315 rounded to exactly two decimal places.

# number = 29.343423
# print(f"{number:.2f}")
# print("%.2f" % number)
