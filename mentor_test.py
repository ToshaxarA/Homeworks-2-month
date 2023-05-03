# """1.	Задание: Создайте программу, которая будет запрашивать у пользователя его
# имя и возраст, а затем выводить приветственное сообщение с использованием этой информации."""

# name = input("Введите Ваше имя: ")
# age = input("Введите Ваш возраст: ")

# print(f"Здравствуйте! {name}, в {age} всё только начинается!")

# """2.	Задание: Напишите программу, которая будет запрашивать у пользователя длины двух
#  сторон прямоугольника, а затем выводить площадь и периметр этого прямоугольник"""

# side_1 = float(input("Введите длинну первой стороны прямоугольника: "))
# side_2 = float(input("Введите длинну второй стороны прямоугольника: "))
# square = side_1*side_2
# perimetr = 2*side_1+2*side_2
# print(f"Площадь прямоугольника: {square}\nПериметр прямоугольника: {perimetr}")

# """3.	Задание: Напишите программу, которая будет принимать список чисел и выводить 
# на экран только те числа, которые больше 10."""

# list_1=[]
# list_2=[]
# arr = tuple(map(int, input("Введите список чисел (через запятую): ").split(',')))
# for el in arr:
#     list_1.append(int(el))
# for i in list_1:
#     if i>10:
#         list_2.append(i)
# print("Числа больше 10:", " ".join(map(str,list_2)))
        
# """4.	Задание: Напишите программу, которая будет запрашивать у пользователя строку и проверять,
# является ли эта строка палиндромом (то есть читается одинаково слева направо и справа налево)."""
# while True:
#     word = input("Введите строку: ")
#     if str(word) == str(word)[::-1] :
#         print("Эта строка является палиндромом")
#     else:
#         print("Эта строка НЕ является палиндромом")

# """5.	Задание: Напишите программу, которая будет запрашивать у пользователя число и выводить 
# на экран таблицу умножения этого числа от 1 до 10."""

# number = int(input("Введите число: "))
# print(f"Таблица умножения для числа {number}:")
# for i in range(1,11):
#     print(f"{number}*{i} = {number*i}")

# """1.Задание: Создайте класс "Собака" (Dog), который имеет атрибуты "имя" (name) и 
# "возраст" (age), а также метод "лай" (bark), который выводит на экран сообщение "Собака <имя> лает!".
# """

# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
#     def bark (self):
#         print(f"Собака {self.name} лает!")
# dog_1 = Dog("Шарик",7)
# dog_2 = Dog("Абдулла",12)

# Dog.bark(dog_1)

# """2.	Задание: Создайте класс "Круг" (Circle), который имеет атрибут "радиус" (radius)
#  и методы "площадь" (area) и "длина окружности" (circumference), которые вычисляют
#   соответствующие значения."""
# import math
# class Circle:
#     def __init__(self, radius) -> None:
#         self.radius = radius
    
#     def radius(self):
#         return self.radius
#     def area(self):
#         square = self.radius*math.pi
#         return square
#     def circumference(self):
#         crf = 2*math.pi*self.radius
#         return crf
# crl_1 = Circle(10)
# crl_2 = Circle(200)
# print(f"Площадь окружности c радиусом {Circle.radius(crl_2)} равна:", Circle.area(crl_2))
# print(f"Длинна окружности c радиусом {Circle.radius(crl_2)} равна:", Circle.circumference(crl_2))
        
# """3.	Задание: Создайте класс "Книга" (Book), который имеет атрибуты "название" (title),
#  "автор" (author) и "год выпуска" (year), а также метод "информация" (info), который выводит
# на экран информацию о книге в формате "<название>, <автор>, <год выпуска>"."""

# class Book:
#     def __init__(self, title,author,year) -> None:
#         self.title = title
#         self.author = author
#         self.year = year
#     def info(self):
#         print(f"{self.title}, {self.author}, {self.year}")

# book_1 = Book("Nineteen Eighty-Four", "Джордж Оруэлл", 1948)
# book_1.info()

# """4.	Задание: Создайте класс "Кошка" (Cat), который имеет атрибуты "имя" (name) и "вес" (weight),
# а также методы "мяуканье" (meow) и "прыжок" (jump), которые выводят на экран сообщения 
# "Кошка <имя> мяукает!" и "Кошка <имя> прыгает!" соответственно."""

# class Cat:
#     def __init__(self, name, weight) -> None:
#         self.name = name
#         self.weight = weight
#     def meow(self):
#         print(f"Кошка {self.name} мяукает!")
#     def jump(self):
#         print(f"Кошка {self.name} весом {self.weight}кг прыгает!")

# cat_1 = Cat("Маруся", 5)
# cat_1.meow()
# cat_1.jump()