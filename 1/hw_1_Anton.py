# ДЗ к 1 уроку 2 месяца Backend
"""ДЗ №1
1. Создать класс Person с атрибутами fullname, age, is_married
2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
6. Добавить в класс Teacher атрибут уровня класса salary
7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
"""
from statistics import mean
class Person:
    """Инициализация атрибутов персоны"""
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        """Вывод основной информации о человеке"""
        print(f"Имя:{self.fullname} Возраст:{self.age} Семейный статус: {self.is_married}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        """Инициализация атрибутов класса родителя, дополнение атрибутом marks"""
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks
        
    def average_rating(self):
        sum=0
        for value in self.marks.values():
            sum=sum+mean(value)
        fin_sum = sum/len(self.marks.values())
        print(f"Средний балл:",fin_sum)
    """Метод для рассчёта и вывода среднего балла по всм предметам"""
    def ocenki(self):
        print(self.marks)
    """Метод для вывода всех оценок по всем предметам"""

Student_1 = Student("Диего", 23, "Single", {"Математика":[5,5,5,5],"Физика":[5,5,5,5,5,5]})
Student_2 = Student("Фёдор", 20, "Married", {"Математика":[2,2,2,2,2],"ОБЖ":[2,3,2,4,5,2]})
Student_3 = Student("Тунгуз", 19, "Single", {"Математика":[3,3,3,3,3,5]})
Student_4 = Student("Нурболот", 22, "Married", {"Математика":[5,5,4,3,5]})
Student_5 = Student("Айзерек", 24, "Divorsed", {"Математика":[5,5,4,3,5]})
Student_6 = Student("Магнус", 11, "Single", {"Математика":[1,1,1,1,3,4], "Английский":[1,1,1,1,1,2]})
Student_7 = Student("Чолпон", 17, "Single", {"Математика":[5,5,4,4,5,5,5]})
list_of_students = [Student_1,Student_2,Student_3,Student_4,Student_5,Student_6,Student_7]

class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary = 0):
        """Инициализация атрибутов класса родителя, дополнение атрибутами experience и salary """
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary

    def zarplata(self):
        standart_zp = float(input("Введите стандартную зарплату: "))
        if self.experience>3:
            fin_zp = standart_zp + standart_zp*(self.experience-3)*0.05
        else:
            fin_zp = standart_zp
        print(fin_zp)

def create_students(smth):
    for i in smth:
        Student.introduce_myself(i), Student.ocenki(i), Student.average_rating(i)        

create_students(list_of_students)
####  Проверка
# person1 = Student("Диего", 23, "Married", {"Математика":[5,5,4,3,5]})
# person1.introduce_myself()
# person1.average_rating()
# person2 = Teacher("Хулио",56,"Divorsed",25)
# person2.introduce_myself() 
# person2.zarplata()


