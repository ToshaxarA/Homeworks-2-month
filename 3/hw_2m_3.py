"""ДЗ №3
1. 'Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
2. 'Добавить сеттеры и геттеры к существующим атрибутам.
3. 'Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические 
вычисления с атрибутами объекта cpu и memory.
4. 'Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
3. 'Добавить сеттеры и геттеры к существующему атрибуту.
4. 'Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, 
в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты 
(например: если при вызове метода передать число 1 и номер телефона, распечатывается текст 
“Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
5. 'Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
6. 'Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал
 симуляцию проложения маршрута до локации.
7. 'В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию 
об объекте.
8. 'Перезаписать все магические методы сравнения в классе Computer, для того чтоб можно было 
сравнивать между собой объекты, по атрибуту memory.
9. 'Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
10. 'Распечатать информацию о созданных объектах
11. 'Опробовать все возможные методы каждого объекта (например: use_gps и тд.)"""

class Computer:
    def __init__(self, cpu=10, memory=23) -> None:
        self.__cpu = cpu
        self.__memory = memory
    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value
    @property
    def memory(self):
        return self.__memory
    @memory.setter
    def memory(self, value):
        self.__memory = value
    
    def make_computations(self):
        a = self.__cpu - self.__memory
        print(a)

    def __str__(self) -> str:
        return f"Процессор: {self.__cpu}, Объём памяти: {self.__memory}"
    
    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory
    
    def __ne__(self, other):
        return self.__memory != other.__memory
    
class Phone:
    def __init__(self, sim_cards_list) -> None:
        self.__sim_cards_list = sim_cards_list
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value
    def call(self, sim_cards_list, call_to_number):
        self.call_to_number=call_to_number
        print(f"Идет звонок на номер {self.call_to_number} с сим-карты-{ self.__sim_cards_list}")

    def __str__(self) -> str:
        return f"Список сим-карт: {self.__sim_cards_list}"
phone1 = Phone("1 - Beeline")    
phone1.call(1,"+996 777 99 88 11")

class SmartPhone(Computer,Phone):
    def __init__(self, cpu, memory, sim_cards_list) -> None:
        Computer.__init__(self,cpu,memory)
        Phone.__init__(self,sim_cards_list)
    
    def use_gps(self, location):
        self.location = location
        print(f"До локации {self.location} осталось 5 минуточек, идите следующим маршрутом...")
    
    def __str__(self) -> str:
        return f"Процессор: {self.cpu}, Объём памяти: {self.memory}, Список сим-карт: {self.sim_cards_list}"

comp1 = Computer(111,23)
ph1 = Phone("3 - MegaCom")
smf1 = SmartPhone(10,21,"1 - Beeline")
smf2 = SmartPhone(11,34,"2 - O!")
list1 = [comp1,ph1,smf1,smf2]

for i in list1:
    print(str(i))

print(Computer.__ne__(comp1,smf2))

# Методы класса Computer:
comp1.make_computations()
print(str(comp1))
print(Computer.__gt__(comp1,smf2))
print(Computer.__lt__(comp1,smf2))
print(Computer.__ge__(comp1,smf2))
print(Computer.__le__(comp1,smf2))
print(Computer.__eq__(comp1,smf2))
print(Computer.__ne__(comp1,smf2))

# Методы класса Phone:
ph1.call(3,"+996 777 99 88 11")
print(str(ph1))

# Методы класса SmartPhone:
smf1.use_gps("Osh")
print(str(smf1))