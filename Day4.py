# --------->Assignment 1
# Ask user for marks
# If marks are 50 or more:
# Pass
# Otherwise:
# Fail

marks = int(input("Enter your marks: "))
if marks >= 50:
    print("Pass")
else:
    print("Fail")


# Ask user for age.
# If age is:
# 18 or more → Adult
# 13 to 17 → Teenager
# Below 13 → Child

age = int(input("Enter your age: "))
if(age >= 18):
    print("Adult")
elif(age >= 13 and age <=17):
    print("Teenegar")
else:
    print("Child")