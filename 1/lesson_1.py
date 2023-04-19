class Transport:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, model, year, color, winks_range):
        Transport.__init__(self, model, year, color)
        self.winks_range = winks_range

    def fly(self, country):
        print(f"{self.model} летит в {country}")


class Car(Transport):  # Шаблон
    number_of_weels = 4  # аттрибуты/поля класса

    # __init__ - Конструктор
    # model, year, color - Входящие параметры
    # self - ссылка на объект
    # self.model - аттрибуты/поля обьекта
    def __init__(self, model, year, color, penalties=0.0):
        Transport.__init__(self, model, year, color)
        self.penalties = penalties

    def drive(self, city):  # Метод
        print(f"{self.model} едет в {city}")


class Truck(Car):
    def __init__(self, model, year, color, load_capacity, penalties=0.0):
        Car.__init__(self, model, year, color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight):
        if weight > self.load_capacity:
            print(f"Ты не можешь загрузить груз, он превыет грузоподьемность {self.load_capacity} кг")
        else:
            print(f"Груз загружен в грузовик {self.model}. Вес - {weight} кг")


transport = Transport("Transport", 2020, "Green")

print(Car.number_of_weels)

tesla_car = Car("Tesla Model X", 2023, "White")  # Объект


print(tesla_car)
print(f"Model: {tesla_car.model} Year: {tesla_car.year} Color: {tesla_car.color} Penalties: {tesla_car.penalties}")
tesla_car.color = "Black"

print(f"Model: {tesla_car.model} Year: {tesla_car.year} Color: {tesla_car.color} Penalties: {tesla_car.penalties}")
tesla_car.change_color("Blue")
print(tesla_car.number_of_weels)
print(f"Model: {tesla_car.model} Year: {tesla_car.year} Color: {tesla_car.color} Penalties: {tesla_car.penalties}")

tesla_car.drive("Ош")
Car.number_of_weels = 8
kamaz = Truck(model="Kamaz", year=1999, color="red", load_capacity=12000)
print(f"Model: {kamaz.model} Year: {kamaz.year} Color: {kamaz.color} "
      f"Penalties: {kamaz.penalties} load_capacity: {kamaz.load_capacity}")

kamaz.drive("Бишкек")
print(kamaz.number_of_weels)
kamaz.load_cargo(111000)


# def create_cars():
#     tesla_car1 = Car("Tesla Model X", 2023, "White")  # Объект
#     tesla_car2 = Car("Tesla Model X", 2023, "White")  # Объект
#     tesla_car3 = Car("Tesla Model X", 2023, "White")  # Объект
#     return [tesla_car1]
#
# for i in create_cars():
#     i.drive()
