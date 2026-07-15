

Students = []

def Add_Student():
    print("\n📌 ----- Add Student -----")
    Student_id = input("Enter Student Id: ")
    for student in Students:
            if student["id"] == Student_id:
                print("❌ Student ID already exists.")
                return
                
    
    name = input("👤 Enter Student Name: ")
    age = int(input("🎂 Enter Student Age: "))
    course = input("📚 Enter Course: ")
    student = {
           "id" : Student_id,
           "name" : name,
           "age" : age,
           "course" : course
    }
    Students.append(student)
    print("✅ Student added successfully.")
            


def view_students():
        if(len(Students) == 0):
            print("❌ No students available.")
            return
        print("-" * 50)
       
        for student in Students:
                print("=" * 45)
                print("\n📋 ----- Student Records -----")
                print("=" * 45)
                print(f"Student ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Course     : {student['course']}")
                print("=" * 45)
        return
        print("❌ No students available.")

       
def search_student():
    print("\n🔍 ----- Search Student -----")

    search_id = input("🆔 Enter Student ID: ")
    for student in Students:
        if student["id"] == search_id:
                print("\n✅ Student Found Successfully")
                print(f"ID           : {student['id']}")
                print(f"Name         : {student['name']}")
                print(f"Age          : {student['age']}")
                print(f"Course       : {student['course']}")
                print("-" * 50)
                return
    print("❌ Student not found.")
                
def update_Student():
    print("\n✏️ ----- Update Student -----")
    update_id = input("🆔 Enter Student ID to Update: ")

    for student in Students:
        if student["id"] == update_id:
            print("Current Details")
            print("\nCurrent Student Details")
            print("-" * 30)
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")

            student['name'] = input("Enter new name")
            student['age'] = input("Enter new age")
            student['course'] = input("Enter new course")
            print("✏️ Student updated successfully.")
            return

    print("❌ Student not found.")


def delete_student():
    print("\n🗑️ ----- Delete Student -----")

    delete_id = input("🆔 Enter Student ID to Delete: ")

    for student in Students:
        if student["id"] == delete_id:
            Students.remove(student)
            print("🗑️ Student deleted successfully.")
            return

    print("❌ Student not found.")



while True:
  

    print("""
============================================================
🎓           STUDENT MANAGEMENT SYSTEM
============================================================

1️⃣  ➕ Add Student
2️⃣  📋 View Students
3️⃣  🔍 Search Student
4️⃣  ✏️ Update Student
5️⃣  🗑️ Delete Student
6️⃣  🚪 Exit

============================================================
""")

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
        print("\n" + "=" * 60)
        print("🙏 Thank you for using Student Management System.")
        print("💻 Developed by Abdul Haseeb")
        print("🌟 Keep Learning, Keep Coding!")
        print("=" * 60)

    else:
        print("Invalid choice! Please try again.")