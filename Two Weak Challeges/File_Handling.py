# Exercise 1: Write User Name to File
# Problem Statement: Write a Python program that accepts a
# user’s name as input and writes it to a file called user.txt.

# newfile = open('Haseeb.txt' , 'x')/

# file = open('Haseeb.txt' , 'w')
# file.write("Hello How are you")
# file.close()
# file = open('Haseeb.txt' , 'w')
# file.write("shut up")
# file.close()

# file = open("Haseeb.txt" , 'r')
# rd = file.read()
# print(rd)
# file.close()


# practice-------------------->

# Exercise 1: Write User Name to File
# Problem Statement: Write a Python program that accepts a user’s name as
# input and writes it to a file called user.txt.
name = input("Enter your name")
newfile = open("newfile.txt" , 'w')
newfile.write(name)

# Exercise 2: Read and Print Complete File
# Problem Statement: Write a Python program that opens
# a file called data.txt and prints its entire contents to the console.

file = open("data.txt" , 'r')
da = file.read()
print(da)


# Exercise 3: Read File Line by Line Using Loop
# Problem Statement: Write a Python program that reads a 
# file called lines.txt and prints each line one at a time using a loop.

with open("lines.txt" , 'r') as files:
    for line in files:
        print(line, end='')

# Exercise 4: Read File Lines into a List
# Problem Statement: Write a Python program
# that reads all lines from a file called items.txt into a list and prints the list.
with open("lines.txt" , "r") as f:
    lines = f.readlines()

print(lines)

# Exercise 5: Append New Sentence to Existing File
# Problem Statement: Write a Python program that appends the sentence
# This is a new line. to an existing file called notes.txt without overwriting its current content.

with open("lines.txt" , 'a') as apnd:
    apnd.write("\nHey! this is new line")
print("Sentence Append successfully!")

# Exercise 6: Clear All File Content
# Problem Statement: Write a Python program that clears all content
# from an existing file called temp.txt, leaving it as an empty file.
with open("NewFile.txt" , 'w') as f:
    pass

print("File content cleared.")

# Exercise 7: Write Text to New File
# Problem Statement: Write a Python program that creates a 
# new file called output.txt and writes three lines of text to it.
lines = ["First line\n", "Second line\n", "Third line\n"]

with open("output.txt" , "w") as f:
    f.writelines(lines)
print("Text written to output.txt")



# Exercise 8: Check If File Exists
# Problem Statement: Write a Python program that checks
# whether a file called data.txt exists in the current 
# directory and prints an appropriate message based on the result.

import os
if os.path.exists("lines.txt"):
    print("File exists.")
else:
    print("File does not exist.")


# Exercise 9: Handle Missing File with Try-Except
# Problem Statement: Write a Python program that attempts 
# to open a file called missing.txt and gracefully handles 
# the case where the file does not exist using a try-except block.

try:
    with open("lines.txt" , 'r') as f:
        content =f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")

# Exercise 10: Count Total Lines in File
# Problem Statement: Write a Python program that opens
# a file called data.txt and counts the total number of lines it contains.
with open("lines.txt" , 'r') as f:
    lines = f.readlines()

print("Total lines: " , len(lines))


# Exercise 11: Count Total Words in File
# Problem Statement: Write a Python program that reads a file
# called data.txt and counts the total number of words across all its lines.


with open("lines.txt" , 'r') as f:
    content = f.read()
Words = content.split()
print("Total words: " , len(Words))

# Exercise 12: Count Total Characters in File
# Problem Statement: Write a Python program that reads a 
# file called data.txt and counts the total number of characters it contains, including spaces and newlines.
with open("lines.txt" , 'r') as f:
    characters = f.read()

print("Total characters: ", len(characters))

# Exercise 13: Count Specific Word Occurrences in File
# Problem Statement: Write a Python program that reads a file called data.txt
# and counts how many times the word Python appears in it

word_to_find = "line"
with open("lines.txt" , 'r') as f:
    content = f.read()
content = content.count(word_to_find)
print(content)
