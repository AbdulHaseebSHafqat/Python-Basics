class Add_student:
    def __init__(self, id, name, age, number):
        self.id = id
        self.name = name
        self.age = age
        self.number = number

    def view_data(self):
        print(f"{self.id}, {self.name}, {self.age}, {self.number}")

    def student_record(self):
        with open("Student_record.txt", "a") as file:
            file.write(f"{self.id},{self.name},{self.age},{self.number}\n")


class Search_student:

    def search_student(student_id):

        found = False

        try:
            with open("Student_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        print("\nStudent Found")
                        print(f"ID: {data[0]}")
                        print(f"Name: {data[1]}")
                        print(f"Age: {data[2]}")
                        print(f"Phone: {data[3]}")

                        found = True
                        break

        except FileNotFoundError:
            print("No student record found.")
            return

        if not found:
            print("Student not found.")


class update_student:

    def update_student(student_id, new_name):

        found = False
        lines = []

        try:
            with open("Student_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        data[1] = new_name
                        found = True

                    lines.append(",".join(data) + "\n")

            with open("Student_record.txt", "w") as file:

                for line in lines:
                    file.write(line)

            if found:
                print("Student updated successfully.")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student record found.")


class delete_student:

    def delete_student(student_id):

        found = False
        lines = []

        try:
            with open("Student_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():
                        found = True
                        continue

                    lines.append(line)

            with open("Student_record.txt", "w") as file:

                for line in lines:
                    file.write(line)

            if found:
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        except FileNotFoundError:
            print("No student record found.")


class add_course:

    def __init__(self, course_id, course_name, course_hour):
        self.course_id = course_id
        self.course_name = course_name
        self.course_hour = course_hour

    def Store_course(self):

        with open("Course_record.txt", "a") as file:
            file.write(
                f"{self.course_id},{self.course_name},{self.course_hour}\n"
            )


class Enroll_students:

    def enroll_students(student_id, course_id):

        student_found = False
        course_found = False
        already_enrolled = False

        # Check student
        try:

            with open("Student_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        student_found = True
                        break

        except FileNotFoundError:
            print("Student record does not exist.")
            return

        # Check course
        try:

            with open("Course_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if course_id == data[0].strip():

                        course_found = True
                        break

        except FileNotFoundError:
            print("Course record does not exist.")
            return

        # Check duplicate enrollment
        try:

            with open("Enrollment_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip() and course_id == data[1].strip():

                        already_enrolled = True
                        break

        except FileNotFoundError:
            pass

        # Enroll student
        if not student_found:

            print("Student not found.")

        elif not course_found:

            print("Course not found.")

        elif already_enrolled:

            print("Student is already enrolled in this course.")

        else:

            with open("Enrollment_record.txt", "a") as file:

                file.write(f"{student_id},{course_id}\n")

            print("Student enrolled successfully.")


class View_courses:

    def view_courses(student_id):

        found = False

        try:

            with open("Enrollment_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        course_id = data[1].strip()

                        try:

                            with open("Course_record.txt", "r") as course_file:

                                for course_line in course_file:

                                    course_data = course_line.strip().split(",")

                                    if course_id == course_data[0].strip():

                                        print(
                                            f"Course ID: {course_data[0].strip()}"
                                        )

                                        print(
                                            f"Course Name: {course_data[1].strip()}"
                                        )

                                        print(
                                            f"Credit Hours: {course_data[2].strip()}"
                                        )

                                        print("------------------")

                                        found = True

                        except FileNotFoundError:
                            print("Course record does not exist.")
                            return

        except FileNotFoundError:
            print("No enrollment record found.")
            return

        if not found:
            print("No courses found for this student.")


class Calculate_result:

    def add_marks(student_id, course_id, marks):

        # Check that student exists
        student_found = False

        try:

            with open("Student_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        student_found = True
                        break

        except FileNotFoundError:
            print("Student record does not exist.")
            return

        if not student_found:
            print("Student not found.")
            return

        # Check enrollment
        enrolled = False

        try:

            with open("Enrollment_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip() and course_id == data[1].strip():

                        enrolled = True
                        break

        except FileNotFoundError:
            print("Enrollment record does not exist.")
            return

        if not enrolled:
            print("Student is not enrolled in this course.")
            return

        # Save marks
        with open("Result_record.txt", "a") as file:

            file.write(f"{student_id},{course_id},{marks}\n")

        print("Marks added successfully.")

    def view_result(student_id):

        found = False

        try:

            with open("Result_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        print(f"Student ID: {data[0]}")
                        print(f"Course ID: {data[1]}")
                        print(f"Marks: {data[2]}")
                        print("--------------------")

                        found = True

        except FileNotFoundError:
            print("No result record found.")
            return

        if not found:
            print("No result found.")

    def calculate_result(student_id):

        total = 0
        count = 0

        try:

            with open("Result_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        marks = int(data[2].strip())

                        total = total + marks
                        count = count + 1

        except FileNotFoundError:
            print("No result record found.")
            return

        if count > 0:

            average = total / count

            print(f"Total Marks: {total}")
            print(f"Average: {average}")

            if average >= 80:
                print("Grade: A")

            elif average >= 70:
                print("Grade: B")

            elif average >= 60:
                print("Grade: C")

            elif average >= 50:
                print("Grade: D")

            else:
                print("Grade: F")

        else:

            print("No result found.")


while True:

    print("\n================================")
    print("    STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Add Course")
    print("7. Enroll Student")
    print("8. View Student Courses")
    print("9. Calculate Result")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    # Add Student
    if choice == "1":

        student_id = input("Enter Student ID: ")

        # Check duplicate ID
        duplicate = False

        try:

            with open("Student_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if student_id == data[0].strip():

                        duplicate = True
                        break

        except FileNotFoundError:
            pass

        if duplicate:

            print("Student ID already exists.")

        else:

            name = input("Enter Name: ")

            age = input("Enter Age: ")

            number = input("Enter Phone Number: ")

            student = Add_student(
                student_id,
                name,
                age,
                number
            )

            student.student_record()

            print("Student added successfully.")

    # View Students
    elif choice == "2":

        try:

            with open("Student_record.txt", "r") as file:

                found = False

                for line in file:

                    data = line.strip().split(",")

                    print(f"ID: {data[0]}")
                    print(f"Name: {data[1]}")
                    print(f"Age: {data[2]}")
                    print(f"Phone: {data[3]}")
                    print("--------------------")

                    found = True

                if not found:
                    print("No students found.")

        except FileNotFoundError:

            print("No student record found.")

    # Search Student
    elif choice == "3":

        student_id = input("Enter Student ID: ")

        Search_student.search_student(student_id)

    # Update Student
    elif choice == "4":

        student_id = input("Enter Student ID: ")

        new_name = input("Enter New Name: ")

        update_student.update_student(
            student_id,
            new_name
        )

    # Delete Student
    elif choice == "5":

        student_id = input("Enter Student ID: ")

        delete_student.delete_student(
            student_id
        )

    # Add Course
    elif choice == "6":

        course_id = input("Enter Course ID: ")

        # Check duplicate course ID
        duplicate = False

        try:

            with open("Course_record.txt", "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if course_id == data[0].strip():

                        duplicate = True
                        break

        except FileNotFoundError:
            pass

        if duplicate:

            print("Course ID already exists.")

        else:

            course_name = input("Enter Course Name: ")

            course_hour = input("Enter Credit Hours: ")

            course = add_course(
                course_id,
                course_name,
                course_hour
            )

            course.Store_course()

            print("Course added successfully.")

    # Enroll Student
    elif choice == "7":

        student_id = input("Enter Student ID: ")

        course_id = input("Enter Course ID: ")

        Enroll_students.enroll_students(
            student_id,
            course_id
        )

    # View Student Courses
    elif choice == "8":

        student_id = input("Enter Student ID: ")

        View_courses.view_courses(
            student_id
        )

    # Calculate Result
    elif choice == "9":

        student_id = input("Enter Student ID: ")

        print("\n1. Add Marks")
        print("2. View Result")
        print("3. Calculate Result")

        result_choice = input("Enter choice: ")

        if result_choice == "1":

            course_id = input("Enter Course ID: ")

            marks = input("Enter Marks: ")

            # Validate marks
            try:

                marks = int(marks)

                if marks < 0 or marks > 100:

                    print("Marks must be between 0 and 100.")

                else:

                    Calculate_result.add_marks(
                        student_id,
                        course_id,
                        marks
                    )

            except ValueError:

                print("Please enter numbers only.")

        elif result_choice == "2":

            Calculate_result.view_result(
                student_id
            )

        elif result_choice == "3":

            Calculate_result.calculate_result(
                student_id
            )

        else:

            print("Invalid result option.")

    # Exit
    elif choice == "10":

        print("Program ended.")

        break

    # Invalid Choice
    else:

        print("Invalid choice. Please try again.")