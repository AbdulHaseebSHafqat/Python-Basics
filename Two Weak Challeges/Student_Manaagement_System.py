class Student:
    def __init__(self, id, name , age, department):
        self.id = id
        self.name = name
        self.age = age
        self.department =department
        self.courses = []

    def st_data(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.department)

    def save_to_file(self):
        with open("Student.txt", 'a') as file:
            file.write(f"{self.id},{self.name},{self.age},{self.department}\n")

    def enroll_course(self, course):
        self.courses.append(course)
        print("Course enrolled successfully")

    def view_courses(self):
        print(f"\nCourses of {self.name}:")

        if len(self.courses) == 0:
            print("No courses enrolled")
            return

        for course in self.courses:
            print(f"Course ID: {course.courde_id}")
            print(f"Course Name: {course.course_name}")
            print(f"Credit Hours: {course.course_hours}")
            print("--------------------")


class Search_Student:
    def search_student(student_id):
        with open("Student.txt" ,'r') as file:
            for line in file:
                data = line.strip().split(",")
                if student_id == data[0]:
                    print(f"ID: {data[0]}")
                    print(f"Name: {data[1]}")
                    print(f"Age: {data[2]}")
                    print(f"Department: {data[3]}")
                    return
            print("Student not found.")
            
class Update_Student:

   
    def update_std(student_id, new_name):

        lines = []

        # Read old data
        with open("Student.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if student_id == data[0]:
                    data[1] = new_name

                lines.append(",".join(data) + "\n")

        # Write updated data
        with open("Student.txt", "w") as file:

            for line in lines:
                file.write(line)

        print("Data updated")

class  Delete_Student:
    def del_std(student_id):
        lines = []
        with open("Student.txt" , 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if student_id == data[0]:
                     continue

                lines.append(line)

            with open("Student.txt", "w") as file:
                for line in lines:
                    file.write(line)
            
        print("Student deleted")            

class Add_Course:
    def __init__(self, course_id , course_name, course_hours):
        self.course_id = course_id
        self.course_name = course_name
        self.course_hours = course_hours

    def add_to_course(self):
        with open('course.txt' , 'a') as file:
            file.write(f"{self.course_id} , {self.course_name} , {self.course_hours}\n")




s1 = Student(101, "Ali" , 12, "BSCS")
s1.st_data()
s1.save_to_file()
Search_Student.search_student("102")
Update_Student.update_std(101, "has")
Delete_Student.del_std("102")
c1 = Add_Course(10, "english", 20.3)
c1.add_to_course()
s1.enroll_course(c1)
s1.view_courses()






# ================================
#    STUDENT MANAGEMENT SYSTEM
# ================================

# 1. Add Student
# 2. View Students
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Add Course
# 7. Enroll Student
# 8. View Student Courses
# 9. Calculate Result
# 10. Save Data
# 11. Exit