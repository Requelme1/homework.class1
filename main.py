class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg_ex_grade(self):
        grades_list = []
        for i in self.grades.values():
            grades_list.extend(i)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_ex_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_ex_grade() < other.get_avg_ex_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_ex_grade() > other.get_avg_ex_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_avg_ex_grade() == other.get_avg_ex_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_avg_ex_grade(self):
        grades_list = []
        for i in self.grades.values():
            grades_list.extend(i)
        return round(sum(grades_list) / len(grades_list), 2)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_ex_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_ex_grade() < other.get_avg_ex_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_ex_grade() > other.get_avg_ex_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_avg_ex_grade() == other.get_avg_ex_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
bad_student = Student('Anton', 'Smirski', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Git']
bad_student.finished_courses += ['Введение в программирование']
cool_reviewer = Reviewer('Some', 'Buddy')
bad_reviewer = Reviewer('No', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

for i in range(4): cool_reviewer.rate_hw(best_student, 'Python', 10)

for i in range(4): cool_reviewer.rate_hw(best_student, 'Git', 10)

bad_reviewer.courses_attached += ['Python']
bad_reviewer.courses_attached += ['Git']

for i in range(4): bad_reviewer.rate_hw(bad_student, 'Python', 8)

for i in range(4): bad_reviewer.rate_hw(bad_student, 'Git', 8)

cool_lecturer = Lecturer('Bob', 'Marley')
bad_lecturer = Lecturer('Petya', 'Krutoi')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

for i in range(4): best_student.rate_lect(cool_lecturer, 'Python', 10)

for i in range(4): best_student.rate_lect(cool_lecturer, 'Git', 10)

bad_lecturer.courses_attached += ['Python']
bad_lecturer.courses_attached += ['Git']

for i in range(4): bad_student.rate_lect(bad_lecturer, 'Python', 7)

for i in range(4): bad_student.rate_lect(bad_lecturer, 'Git', 7)

print(best_student.grades,
      bad_student.grades,
      cool_lecturer.grades,
      cool_reviewer,
      bad_reviewer,
      cool_lecturer,
      bad_reviewer,
      best_student,
      bad_student, sep="\n"
      )

list_student = [bad_student, best_student]
list_lecturer = [bad_lecturer, cool_lecturer]

def student_rank(list_student, course_name):
    rank_list = []
    for student in list_student:
        for mark in student.grades[course_name]:
            rank_list.append(mark)
            if len(rank_list) == 0:
                return 'Ошибка'
        return f'Средняя оценка всех студентов на курсе {course_name} : {round(sum(rank_list) / len(rank_list), 2)}'

def lecturer_rank(list_lecturer, course_name):
    rank_list = []
    for lecturer in list_lecturer:
        for mark in lecturer.grades[course_name]:
            rank_list.append(mark)
            if len(rank_list) == 0:
                return 'Ошибка'
        return f'Средняя оценка всех лекторов на курсе {course_name} : {round(sum(rank_list) / len(rank_list), 2)}'

print(student_rank(list_student, 'Git'),
      student_rank(list_student, 'Python'),
      lecturer_rank(list_lecturer, 'Git'),
      lecturer_rank(list_lecturer, 'Python'), sep="\n"
      )