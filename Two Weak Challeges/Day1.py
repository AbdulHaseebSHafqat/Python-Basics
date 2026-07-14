# --------------->Problem1
# Write a Python function that accepts two integer numbers. If the product of the two numbers
# is less than or equal to 1000, return their product; otherwise, return their sum.

def mul_or_sum(number1 , number2):
    product = number1 * number2 

    if(product <= 1000):
        return product
    else:
        return number1+number2


result = mul_or_sum(20 ,30)
print("The result is", result)

result = mul_or_sum(40, 30)
print("The result is", result)

# --------------->Problem2
# Iterate through the first 10 numbers (0–9). 
# In each iteration, print the current number, the previous number, and their sum.

prev_num = 0
for i in range(10):
    x_sum = prev_num + 1
    print("Current Number", [i] ,"Previous Number", [prev_num], "Sum:",[x_sum] )
    prev_num = i

# --------------->Problem3
# Display only those characters which are present at an even index number in given string.
String =  "pynative"
even_char = String[::3]
for i in even_char:
    print(i)

    
# --------------->Problem4

# Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def remove_char(word, n):
    print('Original string:', word)
    res = word[n:]
    return res


print("Removing characters from a string")
print(remove_char("pynative", 4))
print(remove_char("pynative", 2))


# --------------->Problem5
# Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a = 10
b = 20

swap = a , b = b , a  #comma creates tuple of right side values and then swap on left side
print(swap)  

print("a" , a)
print("b" , b)


# --------------->Problem6
#  Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.
num  = 4
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i

print(f"The factorial of {num} is {factorial}")


# --------------->Problem7
# Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).
 
fruits = ["apple" , "bannana" , "grapes" , "cherry" , "date"]
fruits.append("pineapple")
fruits.pop(1)
print(fruits)

# --------------->Problem8
# Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

text = "Python"
rev_str =text[:: -1]
print(rev_str)

print(f"Original: {text}")
print(f"Reversed: {rev_str}")

# --------------->Problem9
# Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

sentence = "Learning Python is fun!"
vowels = 'aeiou'
count = 0
for char in sentence.lower():
    if char in vowels:
        count += 1


print(f"Number of vowels: {count}")
    
# --------------->Problem10
# Given a list of integers, find and print both the largest and the smallest numbers.

nums = [45, 2, 89, 12, 7]

largest = max(nums)
smallest = min(nums)

print(f"Largest: {largest}")
print(f"Smallest: {smallest}")


# --------------->Problem11
# Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

data = [1, 4, 2, 3, 4, 2, 4, 5]
convert = set(data)

print(f"Unique List: {convert}")

# --------------->Problem12
# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.


def first_last_num(list_of_num):
    print("Given list:", list_of_num)

    if list_of_num[0] == list_of_num[-1]:
        return True
    else:
        return False



numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_num(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_num(numbers_y))


# --------------->Problem13
# Iterate through a given list of numbers and print only those numbers which are divisible by 5.

num_list = [10, 20, 33, 46, 55]
for i in num_list:
    if(i%5 == 0):
        print(i)
        i+=1


# --------------->Problem14
# Write a program to find how many times the substring “Emma” appears in a given string.

str_x = "Emma is good developer. Emma is a writer"
count = str_x.count("Emma")

print(count)


# --------------->Problem15
# Print the following pattern where each row contains a number repeated a 
# specific number of times based on its value.

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for num in range(1,6):
    for i in range(num):
        print(num, end=" ")
    print("\n")


# --------------->Problem16
# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

def check_palid(num):
    num = str(num)
    if(num == num[::-1]):
        print("palidram" ,num)
    else:
        print("no palidram" , num)


check_palid(121)
check_palid(123)


# --------------->Problem17
# Create a new list from two given lists such that the new list contains odd numbers from
# the first list and even numbers from the second list.


def merge_list(list1 , list2):
    result_list = []

    for num in list1:
        if num%2 != 0:
            result_list.append(num)

    for num in list2:
        if num%2 == 0:
            result_list.append(num)

    return result_list



list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print("result list:", merge_list(list1, list2))


# --------------->Problem18
# Write a program to extract each digit from an integer in the reverse order.

number = 7564
print("Given Number: ", number)
while number>0:
    digit = number % 10

    number = number // 10  
    print(digit, end=" ")

# --------------->Problem20
# Print a multiplication table from 1 to 10 in a formatted grid.

# for i in range(1 , 11):
#     for j in range(1 , 11):
#         print(i * j, end="\t")
#     print("\n")
print("\n")
for i in range(1, 11):
    for j in range(1, 11):
        # Print product followed by a tab space
        print(i * j, end="\t")
    print("\n")
    

# --------------->Problem21
# Learn about reverse indexing. Controlling loop boundaries in reverse is 
# important for algorithms that process data from end to beginning.
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

for i in range(5 ,0 , -1):
    for j in range(i):
        print("*", end="")
    print("\n")


# --------------->Problem23
#  Write a program to check if a given number is a palindrome.
#  A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

number = 12221

str_number = str(number)
if(str_number == str_number[::-1]):
    print("Yes. given number is palindrome number")
else:
     print("No. given number is not palindrome number")


# --------------->Problem23
# Write a program to print the first 15 terms of the Fibonacci series.
# The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.


number1 = 0 
number2 = 1
for i in range(15):
    print(number1, end="  ")
    res = number1 + number2

    number1 = number2
    number2 = res


# --------------->Problem25
# Write a program that takes a year as input and determines if it is a leap year.
year = int(input("Enter an Year"))
if(year % 4 == 0 and year % 100 != 0) or (year%400 == 0):
    print("leap Year")
else:
    print("Not a leap year")

# --------------->Problem26
# Write a program that takes two separate dictionaries and merges them into one single dictionary.

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

merge_dict = dict1 | dict2
print(merge_dict)


# --------------->Problem27
# Take two lists and find the elements that appear in both. Use Sets to perform the operation.

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

seta = set(list_a)
setb = set(list_b)

common = seta & setb
print(f"Common Elements: {common}")