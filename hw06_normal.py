# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, family_name, name, second_name):
        self.family_name = family_name
        self.name = str(name[0]) + '.'
        self.secondname = str(second_name[0]) + '.'
    @property
    def full_name(self):
        return f"{self.family_name} {self.name}{self.secondname}"

class Subject:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, subject, family_name, name, second_name):
        self.subject = subject
        super().__init__(family_name, name, second_name)

class Student(Person):
    def __init__(self, family_name, name, second_name, mother, father):
        super().__init__(family_name, name, second_name)
        self.mother = mother.full_name
        self.father = father.full_name

class Classroom:
    def __init__(self, number, students, teachers):
        self.number = number
        self.teachers = teachers
        self.students = students

class School:
    def __init__(self):
        self.classes = classes
    def get_classes(self):
        return [x.number for x in self.classes]
    def get_students(self, classnumber):
        students = [x.students for x in self.classes if x.number == classnumber]
        return [x.full_name for x in students[0]]
    def get_student_class(self, studentname):
        classnumber = [x for x in self.classes if studentname in [y.full_name for y in x.students]]
        return [x.number for x in classnumber]
    def get_subjects(self, studentname):
        classes = [x for x in self.classes if studentname in [y.full_name for y in x.students]]
        return [x.subject.name for x in classes[0].teachers]
    def get_teachers(self, classnumber):
        teachers = [x.teachers for x in self.classes if x.number == classnumber]
        return [x.full_name for x in teachers[0]]
    def get_parents(self, studentname):
        students = [x.students for x in self.classes if studentname in [y.full_name for y in x.students]]
        students = [x for x in students[0] if studentname == x.full_name]
        return [students[0].mother, students[0].father]

mother1 = Person("Иванова", "Ольга", "Петровна")
father1 = Person("Иванов", "Иван", "Иванович")
student1 = Student("Иванов", "Дмитрий", "Иванович", mother1, father1)

mother2 = Person("Сидорова", "Татьяна", "Николаевна")
father2 = Person("Сидоров", "Роман", "Иванович")
student2 = Student("Сидоров", "Алексей", "Романович", mother2, father2)

mother3 = Person("Орлова", "Наталья", "Михайловна")
father3 = Person("Орлов", "Сергей", "Петрович")
student3 = Student("Орлов", "Петр", "Петрович", mother3, father3)

mother4 = Person("Петрова", "Ольга", "Михайловна")
father4 = Person("Петров", "Иван", "Александрович")
student4 = Student("Петрова", "Олеся", "Ивановна", mother4, father4)

math = Subject("Математика")
english = Subject("Англмйский язык")
chemestry = Subject("Химия")

math_teacher = Teacher(math, "Васильева", "О", "П")
english_teacher = Teacher(english, "Борисова", "О", "П")
chemestry_teacher = Teacher(chemestry, "Дмитриева", "О", "П")

class1_students = [student1, student2]
class1_teachers = [math_teacher]
class1 = Classroom("6A", class1_students, class1_teachers)

class2_students = [student3]
class2_teachers = [english_teacher, chemestry_teacher]
class2 = Classroom("7Б", class2_students, class2_teachers)

class3_students = [student4]
class3_teachers = [math_teacher, chemestry_teacher]
class3 = Classroom("8В", class3_students, class3_teachers)

classes = [class1, class2, class3]
school = School()
print("Классы школы: ", school.get_classes())
classnumber = "8В"
print("\n")
print(f"Ученики класса {classnumber} ", school.get_students(classnumber))

studentname = "Орлов П.П."
studentclass = school.get_student_class(studentname)
print("\n")
print(f"Ученик {studentname}")
print("Класс", studentclass)
print("Учителя ученика:", school.get_teachers(studentclass[0]))
print("Предметы ученика: ", school.get_subjects(studentname))
print(f"Родители ученика {studentname} ", school.get_parents(studentname))
print("\n")
print(f"Учителя класса {classnumber} ", school.get_teachers(classnumber))