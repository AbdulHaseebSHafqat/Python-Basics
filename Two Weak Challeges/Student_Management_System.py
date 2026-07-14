print("===========Student Management System===========")
# print("1. Add Student")
# print("2. View Students")
# print("3. Search Student")
# print("4. Update Student")
# print("5. Delete Student")
# print("6. Exit")

Students = []

def Add_Student():
    print("\n----- Add Student -----")
    Student_id = input("Enter Student Id: ")
    for student in Students:
            if student["id"] == Student_id:
                print("Student id already exist")
                return
                
    
    name = input("Enter Student Name: ")
    age = (input("Enter Student Age: "))
    course = input("Enter Course: ")
    student = {
           "id" : Student_id,
           "name" : name,
           "age" : age,
           "course" : course
    }
    Students.append(student)
    print("Student Added Successfully")
            


def view_students():
        if(len(Students) == 0):
            print("Have 0 student")
            return
        print("-" * 50)
       
        for student in Students:
               print(f"ID           : {student['id']}")
               print(f"Name         : {student['name']}")
               print(f"Age          : {student['age']}")
               print(f"Course       : {student['course']}")

               print("-" * 50)

       
def search_student():
    print("\n----- Search Student -----")

    search_id = input("Enter Student ID: ")
    for student in Students:
          if student["id"] == search_id:
                print(f"Student Found")
                print(f"ID           : {student['id']}")
                print(f"Name         : {student['name']}")
                print(f"Age          : {student['age']}")
                print(f"Course       : {student['course']}")

                print("-" * 50)
                
def update_Student():
    print("\n----- Search Student -----")
    update_id = input("Enter id to update")

    for student in Students:
        if student["id"] == update_id:
            print("Current Details")
            print(student)

            student['name'] = input("Enter new name")
            student['age'] = input("Enter new age")
            student['course'] = input("Enter new course")
            print("Student updated successfully!")
            return

        print("Student not found.")


def delete_student():
    print("\n----- Delete Student -----")

    delete_id = input("Enter Student ID: ")

    for student in Students:
        if student["id"] == delete_id:
            Students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")



while True:

    print("\n")
    print("=" * 35)
    print(" STUDENT MANAGEMENT SYSTEM ")
    print("=" * 35)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        Add_Student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_Student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System.")
        print("Good Bye!")
        break

    else:
        print("Invalid choice! Please try again.")