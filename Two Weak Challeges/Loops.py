# Print first 10 natural numbers using while loop

i = 1
while i <= 10:
    print(i)
    i+=1

# Display numbers from -10 to -1 using for loop

for i in range(-10 , 0):
    print(i)


# Write a program to display a message “Done” after the successful execution 
# of a for loop that iterates from 0 to 4.

for i in range(5):
    print(i)
else:
    print("done!")


# Calculate the sum of all numbers from 1 to N

n = int(input("Enter the number to stop: "))

s = 0
for i in range(n+1):
    s += i

print("Sum is:", s)


# Print multiplication table of a given number
table = int(input("Enter the table to calculate: "))
for i in range(1, 11):
    print(f"{table} * {i} = {table*i}")


# Calculate the cube of all numbers from 1 to a given number

n = int(input("Enter a number: "))
for i in range(n+1):
    print(f"Current number is: {i} and the cube is {i** 3}")

# Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if(item > 500):
        break
    if(item > 150):
        continue
    if item % 5 == 0:
        print(item)


list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0

for num in list1:
    if num == target:
        count += 1
print(f"{target} appears {count} times")


# Print elements from a list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1 , len(my_list) , 2):
    print(my_list[i] , end=" ")


# Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)




# Write a program that counts the total number of vowels and consonants 
# in a given sentence, ignoring spaces and special characters.

sentence = "Loops are Fun!"
vowels = 'aeiou'
v_count = 0
c_count = 0
for char in sentence.lower():
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowerls: ", v_count)
print("Constant: ", c_count)



# Count total number of digits in a number

integer = 75869213123

count = 0

while (integer!= 0):
    integer = integer // 10
    count += 1

print(count)


# Write a program to reverse a given integer number (e.g., 76542 should become 24567).

num = 342445
reverse_number = 0

while num > 0:
    digit =  num % 10
    reverse_number = (reverse_number*10) + digit
    num = num // 10

print(reverse_number)


# Find largest and smallest digit in a number

num = 75869
largest = 0
smallest = 9

while num > 0:
    digit = num%10
    if digit > largest:
        largest = digit
    
    if digit < smallest:
        smallest = digit

    num = num // 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)


# Check if a number is a palindrome

number = 1221
temp = number
reverse_num = 0
while number != 0:
    digit = number %10
    reverse_num = (reverse_num * 10) + digit
    number = number // 10

if temp == reverse_num:
    print("Yes. Given number is palindrome number")
else:
    print("No. Given number is not palindrome")

    

# imp

# Print list in reverse order using a loop
# use of "reversed" keyword
# list1 = [10, 20, 30, 40, 50]
# for i in reversed(list1):
#     print(i)
