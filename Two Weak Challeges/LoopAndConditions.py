# Exercise 1. Print first 10 natural numbers using while loop
# Practice Problem: Write a program to print the first 10 natural
# numbers using a while loop. Each number should be printed on a new line.
i = 1
while i <=10:
    print(i)
    i+=1

# Exercise 2. Display numbers from -10 to -1 using for loop
# Practice Problem: Write a program to display numbers from -10 to -1 using a for loop.
for i in range(-10 , 0):
    print(i)

# Exercise 3. Display a message “Done” after successful execution of for loop
# Practice Problem: Write a program to display a message “Done” after the successful execution 
# of a for loop that iterates from 0 to 4.

for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 4. Calculate the sum of all numbers from 1 to N
# Practice Problem: Write a program that accepts a number 
# from the user and calculates the sum of all numbers from 1 up to that number.

number = int(input("Enter a number: "))
s = 0

for i in range(number+1):
    s += i

print(f"Sum is: {s}")


# Exercise 4. Print multiplication table of a given number
# Practice Problem: Create a program that takes an integer 
# and prints its multiplication table from 1 to 10.

number = int(input("Enter a number for multiplication: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Exercise 6. Calculate the cube of all numbers from 1 to a given number
# Practice Problem: Write a program that takes an integer n and prints the 
# cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

number = int(input("Enter a number for cube: "))

for i in range(1 ,number+1):
    print(f"Current number is : {i} and the cube is {i ** 3}")


# Exercise 7. Display numbers from a list using a loop
# Practice Problem: Given a list of numbers, iterate through it
#  and print numbers that satisfy these conditions:
# The number must be divisible by five.
# If the number is greater than 150, skip it and move to the next.
# If the number is greater than 500, stop the loop entirely.

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
   
    if i > 150:
        continue
    
    if i % 5 == 0:
        print(i)

# Exercise 8. Count occurrences of a specific element in a list
# Practice Problem: Given a list of numbers, use a loop to count
# how many times a specific number (e.g., 10) appears.

list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0
for i in list1:
    if target == i:
        count += 1

print(target , "Appears ", count, "Times")

# Exercise 9. Print elements from a list present at odd index positions
# Practice Problem: Given a Python list, use a loop to print only the 
# elements that are located at odd index positions (index 1, 3, 5, etc.).

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1 , len(my_list), 2):
    print(my_list[i] , end=","  "\n")



# Exercise 10. Print list in reverse order using a loop
# Practice Problem: Given a list, iterate it in reverse 
# order and print each element.

list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)- 1, -1 , -1):
    print(list1[i])

# Exercise 11. Reverse a string using a for loop (no slicing)
# Practice Problem: Write a program that takes a string and 
# reverses it using a for loop. While Python’s [::-1] shortcut 
# is famous, reversing a string manually is a classic way to 
# understand how sequences are constructed.

string = "Python"
reversed_string = ""

for i in string:
    reversed_string = i + reversed_string


print(f"Original: {string}")
print(f"Reversed: {reversed_string}")


# Exercise 12. Count vowels and consonants in a sentence
# Practice Problem: Write a program that counts the total
# number of vowels and consonants in a given sentence, ignoring spaces and special characters.

sentence = "Loops are Fun!"
vowels = 'aeiou'
v_count = 0
c_count = 0
for i in sentence.lower():
    if i.isalpha():
        if i in vowels :
            v_count += 1
        else:
            c_count += 1


print(v_count)
print(c_count)

# Exercise 13. Count total number of digits in a number
# Practice Problem: Write a program to count the total 
# number of digits in a given integer using a while loop.


number = 75869
count = 0

while(number != 0):
    number = number // 10

    count += 1

print("Total numbers: ", count)


# Exercise 14. Reverse an integer number
# Practice Problem: Write a program to reverse a given integer number (e.g., 76542 should become 24567).

number = 76542
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = (reverse_number * 10) + digit

    number = number//10

print(reverse_number)


# Exercise 15. Find largest and smallest digit in a number
# Practice Problem: Write a program to find the largest and
# smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

integer = 75869

L_digit = 0
S_digit = 9

while integer > 0:
    digit = integer %10
    if digit > L_digit:
        L_digit = digit
    if digit < S_digit:
        S_digit = digit
    integer = integer // 10
print(f"Smallest Digit = {S_digit}")
print(f"Largest Digit = {L_digit}")



# Exercise 16. Check if a number is a palindrome
# Practice Problem: Write a program to check if a given number
# is a palindrome. A palindrome number is a number that remains
# the same when its digits are reversed (e.g., 121, 343).

number = 121
temp = number
reverse_number = 0

while number > 0:
    digit = number % 10
    reverse_number = (reverse_number * 10) + digit
    number = number // 10

if temp == reverse_number:
    print(f"number is Palidrom: {temp}")
else:
    print(f"number is not Palidrom: {temp}")

# Exercise 17. Find factorial of a number
# Practice Problem: Write a program to use a loop to
# find the factorial of a given number (e.g., 5!).
# The factorial of N is the product of all integers from 1 to N.

number = 5
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i
print(f"The factorial of {number} is {factorial}")



# Exercise 20. Print right-angled triangle Number Pattern using a Loop
# Practice Problem: Write a program to print a right-angled triangle
# pattern where each row contains increasing numbers up to the row number.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1 , i+1):
        print(j, end=" ")   
    print("")



# Exercise 21. Print the decreasing pattern
# Practice Problem: Write a program to use for loop to print the following reverse number pattern:

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

print("")
for i in range(5 ,0  , -1):
    for j in range(i , 0 , -1):
        print(j, end=' ')
    # New line after each row
    print("")

# Exercise 22. Print the alternate numbers pattern

# Practice Problem: Write a program to print a pattern of alternate numbers from 1 to 20 (e.g., 1, 3, 5…).

for i in range(1, 21, 2):
    print(i, end=" ")



# Exercise 24. Hollow square pattern
# Practice Problem: Print a 5*5 square of stars where the middle is empty, leaving only the border.
print("")


for i in range(5):
    for j in range(5):
        if i == 0 or i == 5 - 1 or j == 0 or j==5 -1:
            print("*", end=' ')
        else:
            print(" ", end=" ")
    print()


