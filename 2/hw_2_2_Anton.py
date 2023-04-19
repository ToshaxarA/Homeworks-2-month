"""ДЗ №2
1. Создать класс Figure (фигура) с атрибутом уровня класса unit (единица измерения величин) и присвоить ему значение cm (сантиметры) или mm (миллиметры)
2. В конструкторе класса Figure должен быть только 1 входящий параметр self, то есть не должно быть атрибутов уровня объекта.
3. Добавить в класс Figure нереализованный публичный метод calculate_area (подсчет площади фигуры)
4. Добавить в класс Figure нереализованный публичный метод info(вывод полной информации о фигуре)
5. Создать класс Circle (круг), наследовать его от класса Figure.
6. Добавить в класс Circle атрибут radius (радиус круга), атрибут должен быть приватным.
7. В классе Circle переопределить метод calculate_area, который бы считал и возвращал площадь круга.
8. В классе Circle переопределить метод info, который бы распечатывал всю информацию о круге следующим образом: Например - Circle radius: 2cm, area: 12.57cm.
9. Создать класс RightTriangle (прямой треугольник - 90 градусов), наследовать его от класса Figure.
10. Добавить в класс RightTriangle атрибут side_a (сторона а) и side_b (сторона б), атрибуты должны быть приватными.
11. В классе RightTriangle переопределить метод calculate_area, который бы считал и возвращал площадь треугольника.
12. В классе RightTriangle переопределить метод info, который бы распечатывал всю информацию о треугольнике следующим образом:Например - RightTriangle side a: 5cm, side b: 8cm, area: 20cm.
13. В исполняемом файле создать список из 2-х разных кругов и 3-х разных треугольников
14. Затем через цикл вызвать у всех объектов списка метод info"""


import math
class Figure:
    unit = "mm"
    def __init__(self) -> None:
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Circle(Figure):
    def __init__(self,radius) -> None:
        self.__radius = radius
    
    # @property
    # def radius(self):
    #     return self.__radius
    
    # @radius.setter
    # def radius(self,value):
    #     self.__radius = value
    
    def calculate_area(self):
        self.area = self.__radius*math.pi**2
        return self.area

    def info(self):
        print(f"Circle radius: {self.__radius}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}.")

class RightTriangle(Figure):
    def __init__(self,side_a,side_b) -> None:
        self.__side_a = side_a
        self.__side_b = side_b
        
    @property
    def side_a(self):
        return self.__side_a
    @side_a.setter
    def side_a(self,value):
        self.__side_a = value
    @property
    def side_b(self):
        return self.__side_b
    @side_a.setter
    def side_b(self,value):
        self.__side_b = value

    def calculate_area(self,side_a,side_b):
        self.area = self.__side_a*self.__side_b*0.5
        return self.area

    def info(self):
        print(f"rightTriangle side a: {self.__side_a}{Figure.unit}, side b: {self.__side_b}{Figure.unit}, area: {self.calculate_area(self.__side_a,self.__side_b)}{Figure.unit}**2")

        pass
    
rightTriangle1 = RightTriangle(6,8)
rightTriangle2 = RightTriangle(25,12)
circle1=Circle(10)
circle2=Circle(20)
circle3=Circle(30)

list1 = [rightTriangle1,rightTriangle2,circle1,circle2,circle3]

for i in list1:
    i.info()