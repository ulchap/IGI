class PrintableMixin:
    def print_info(self):
        for key, value in self.__dict__.items():
            print(f'{key}: {value}')


class Person:
    # def __init__(self, name, birth_date, birth_month, birth_year):
    #     self.name = name
    #     self.birth_date = birth_date
    #     self.birth_month = birth_month
    #     self.birth_year = birth_year

    def __init__(self, person_data):
        self.student_data = person_data

    # def __str__(self):
    #     return f"{self.name} - {self.birth_date}.{self.birth_month}.{self.birth_year}"

class Student(Person, PrintableMixin):
    def __init__(self, student_data, grade):
        super().__init__(student_data)
        self._grade = grade

    def __str__(self):
        return f"{self.student_data} - grade: {self.grade}"

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        self._grade = new_grade

    @property
    def is_honor_student(self):
        return self.grade >= 9
    
    def get_student_data(self):
        return self.student_data

    def update_student_data(self, key, value):
        self.student_data[key] = value
