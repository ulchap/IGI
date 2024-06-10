from student import Student
from school import School

filenamePckl = "students.pkl"
filenameCsv = "students.csv"

students = [
    {"name": "Tom", "birth_date": 28, "birth_month": 1, "birth_year": 2005},
    {"name": "Alice", "birth_date": 15, "birth_month": 2, "birth_year": 2004},
    {"name": "Mark", "birth_date": 11, "birth_month": 3, "birth_year": 2005},
    {"name": "Ann", "birth_date": 22, "birth_month": 4, "birth_year": 2005},
    {"name": "Victor", "birth_date": 20, "birth_month": 5, "birth_year": 2005},
    {"name": "Jane", "birth_date": 6, "birth_month": 6, "birth_year": 2004},
    {"name": "Mia", "birth_date": 5, "birth_month": 7, "birth_year": 2004,},
    {"name": "Max", "birth_date": 14, "birth_month": 7, "birth_year": 2005},
    {"name": "Loo", "birth_date": 13, "birth_month": 7, "birth_year": 2005},
]

student1 = Student(students[0], 5)
student2 = Student(students[1], 7)
student3 = Student(students[2], 10)
student4 = Student(students[3], 10)
student5 = Student(students[4], 9)
student6 = Student(students[5], 4)
student7 = Student(students[6], 4)
student8 = Student(students[7], 8)

school = School() 
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.add_student(student4)
school.add_student(student5)
school.add_student(student6)
school.add_student(student7)
school.add_student(student8)

pickle_school = School()
csv_school = School()

school.save_csv(filenameCsv)
csv_school.load_csv(filenameCsv)

school.save_pickle(filenamePckl)
pickle_school.load_pickle(filenamePckl)

print("Pickle file data:\n")
for student in pickle_school.students:
    print(student)

# Проверка свойства is_honor_student
for student in school.students:
    name = student.student_data['name']
    if student.is_honor_student:
        print(f"{name} - отличник")
    else:
        print(f"{name} - не отличник")

#список учеников, рожденных в месяце, введенном с клавиатуры
while True:
    try:
        month = int(input("Введите месяц: "))
        if (month > 12 or month < 1):
            raise ValueError("Некорректные данные!\n")
        break
    except ValueError as err:
            print(err)
            print("Incorrect input! Try again.")

filtered = school.filter_by_birth_month(month)
for student in filtered:
    student.print_info()

