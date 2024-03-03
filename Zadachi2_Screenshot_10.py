class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def calculate_average_grade(self):
        if len(self.subjects) > 0:
            total_grades = 0
            for subject in self.subjects:
                total_grades += subject['grade']
            average_grade = total_grades / len(self.subjects)
            return average_grade
        else:
            return None


student1 = Student("Павел", 20)
student2 = Student("Влад", 22)

student1.add_subject({"name": "География", "grade": 4})
student1.add_subject({"name": "Физика", "grade": 5})
student2.add_subject({"name": "Русский", "grade": 3})

student1.remove_subject({"name": "География", "grade": 4})

average_grade_student1 = student1.calculate_average_grade()
average_grade_student2 = student2.calculate_average_grade()

print(f"Средний балл студента {student1.name} составляет {average_grade_student1}")
print(f"Средний балл студента {student2.name} составляет {average_grade_student2}")
