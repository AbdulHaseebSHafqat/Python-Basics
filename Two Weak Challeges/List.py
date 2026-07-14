# Exercise 1. Perform Basic List Operations
# Practice Problem: Write a script to perform the following three operations on given list

# Access the third element of a list
# List Length: Print the total number of items
# Check if the list is empty


numbers = [10, 20, 30, 40, 50]

print(f"Third element of a list: {numbers[2]}")
print(len(numbers))
is_empty = len(numbers) == 0
print(f"Is the list empty? {is_empty}")


# Exercise 2. Perform List Manipulation
# Practice Problem: Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.

Initial_List = [100, 50, 400, 500]
Initial_List[1] = 200
print(f"Updated (Change) {Initial_List}")

Initial_List.append(600)
print(f"Updated (Append) {Initial_List}")

Initial_List.insert(2, 300)
print(f"Updated (Insert) {Initial_List}")

Initial_List.remove(600)
print(f"Updated (remove) {Initial_List}")

Initial_List.pop(0)
print(f"Updated (pop) {Initial_List}")


# Exercise 3. Sum and Average of All Numbers in a List
# Practice Problem: Calculate the total sum of all
# integers in a list and find the arithmetic mean (average).
Numbers = [10, 20, 30, 40, 50]
total_sum = sum(Numbers)
average = total_sum/ len(Numbers)

print(f"Sum: {total_sum}")
print(f"Average: {average}")


# Exercise 4. Find Maximum and Minimum from List
# Practice Problem: Identify the largest and smallest numerical values within a provided list.

Data = [45, 12, 89, 2, 67]

maximum = max(Data)
minimum = min(Data)
print(f"largest : {maximum}")
print(f"Smalles : {minimum}")

# Exercise 5. Calculate the Product of All Elements
# Practice Problem: Multiply every number in a list together to find the total product.

Factors = [2, 3, 5, 7]
product = 1
for i in Factors:
    product *= i

print(f"Product = {product}")


# Exercise 6. Count Even and Odd Numbers
# Practice Problem: Given a list of integers, 
# iterate through the items and count how many are even and how many are odd.

Numbers = [10, 21, 4, 45, 66, 93, 11]
E_count = 0
O_count = 0

for i in Numbers:
    if i%2 == 0:
        E_count += 1
    else:
        O_count += 1

print(f"Even Numbers : {E_count}")
print(f"Odd Numbers : {O_count}")


# Exercise 7. Reverse a List
# Practice Problem: Take a list and reverse the order of its elements.

List = [100, 200, 300, 400, 500]

reversed_List = List[:: -1]
print(reversed_List)


# Exercise 8. Sort a List of Numbers
# Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

Unsorted = [56, 12, 89, 3, 22]
new_list = sorted(Unsorted)
print(new_list)

# Exercise 9. Create a Copy of a List
# Practice Problem: Create a copy of an existing list
# so that modifying the copy does not change the original.

Original = ["Apple", "Banana", "Cherry"]

new_copy = Original.copy()
new_copy.append("Data")

print(f"Original: {Original}")
print(f"Copy: {new_copy}")

# Exercise 10. Combine Two Lists
# Practice Problem: Merge two separate lists into a single, unified list.

List_A = ["Physics", "Chemistry"]
List_B = ["Maths", "Biology"]

combined = List_A + List_B
print(f"Combined List: {combined}")

# Exercise 11. List Slicing: Extract Middle Elements
# Practice Problem: Given a list, extract a “slice” containing the middle three elements.

List = [10, 20, 30, 40, 50, 60, 70]

middleThree = List[2:5]

print(f"MiddleThree : {middleThree}")


# Exercise 12. Swap Two Elements at Given Indices
# Practice Problem: Write a script to swap the positions
# of two elements in a list based on their indices.

List = [23, 65, 19, 90]
idx1 , idx2  = 0 ,2

print(f"Original: {List}")

List[idx1] , List[idx2] = List[idx2] , List[idx1]


print(f"Swapped: {List}")

max(wo)