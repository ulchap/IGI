import pickle
import csv

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.students, file)

    def load_pickle(self, filename):
        with open(filename, 'rb') as file:
            self.students = pickle.load(file)

    def save_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            columns = ["name", "birth_date", "birth_month", "birth_year"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            for student in self.students:
                writer.writerow(student.student_data)

    def load_csv(self, filename):
        with open(filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row["name"], "-", row["birth_date"], row["birth_month"], "-", row["birth_year"])


    def filter_by_birth_month(self, month):
        return [student for student in self.students if student.student_data['birth_month'] == month]
    
# users = [
#     {"name": "Tom", "age": 28},
#     {"name": "Alice", "age": 23},
#     {"name": "Bob", "age": 34}
# ]
 
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()
     
#     # запись нескольких строк
#     writer.writerows(users)
     
#     user = {"name" : "Sam", "age": 41}
#     # запись одной строки
#     writer.writerow(user)
 
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], "-", row["age"])
