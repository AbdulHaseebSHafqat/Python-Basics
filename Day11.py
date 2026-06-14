# -------->Assignment 1
# Create a file:
# student.txt
# Write:
# Abdul Haseeb
# Superior University

file = open("data.txt" , "w")
content = file.write("Hello My name is Haseeb\n")
content = file.write("I am currently in the 6th semester at Superior University")
file.close()


# ---------->Assignment 2
# Read the file and print its contents.

file = open("data.txt" , "r")
content = file.read()
print(content)
file.close()

# ---------->Assignment 3
# Append:
# Semester 6
# to the file.
# Then read and print the updated file.

file = open("data.txt" , 'a')
content = file.write("I am currently in 6th semster")
file.close()