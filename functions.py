students = []


def get_students():
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title())
        return students_titlecase
    students_titlecase_names = get_students_titlecase()
    print(students_titlecase_names)


def add_student(name, student_id=0000):
    student = {"name": name, "student_id": student_id}
    students.append(student)


insert_student = input("Would you like to enter a student to the Databse? (y for yes and n for no)\n")


while insert_student == 'y':

    student_list = get_students_titlecase()
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    add_student(student_name, student_id)
    insert_student= input("Would you like to add another student? (y for yes and n for no)\n")

print_students_titlecase()
