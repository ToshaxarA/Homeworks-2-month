class Address:
    def __init__(self, city, street, home_number) -> None:
        self.__city = city
        self.__street = street
        self.__home_number = home_number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if type(value) == str:
            self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        if type(value) == str:
            self.__street = value

    @property
    def home_number(self):
        return self.__home_number

    @home_number.setter
    def home_number(self, value):
        if type(value) == str:
            self.__home_number = value


class Animal:
    def __init__(self, name: str, age: int, address: Address) -> None:
        if not type(name) == str:
            raise Exception("Параметр name принимает только строку!")
        if not type(age) == int and age > 1:
            raise Exception("Параметр age принимает только число!!")
        if not type(address) == Address:
            raise Exception("Параметр address принимает только объект класса Address!")
        self.address = address
        self.__name = name
        self.__age = age  # (public, private)
        self.__created()

    def __created(self):
        print("New animal crated!")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def set_age(self, value):
        if value >= 1: 
            self.__age = value
        else:
            print("Значение не может быть меньше нуля!")

    def info(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nAddress {self.address.city}, street {self.address.street}, №{self.address.home_number}\n"


class Dog(Animal):
    def __init__(self, name: str, age: int, address: Address, commands) -> None:
        super().__init__(name, age, address)
        self.commands = commands

    def speak(self):
        print(f"Dog {self.get_name()} Gav Gav")

    def info(self):
        return super().info() + f"Commands {self.commands}\n\n"

class Cat(Animal):
    def __init__(self, name: str, age: int, address: Address) -> None:
        super().__init__(name, age, address)

    def speak(self):
        print(f"Cat  {self.get_name()} says Meow Meow")


address1 = Address("Bishkek", "Ibraimova", 103)
cat1 = Cat("Barsik", 2, address1)
cat2 = Cat("Timofei", 2, address1)
cat3 = Cat("Snezhok", 2, address1)
dog1 = Dog("Ak-Tosh", 4, address1, ['sit'])
dog2 = Dog("Muhtar", 4, address1, ['aport'])
dog3 = Dog("Sharik", 4, address1, [])
animal_list = [cat1, dog1, dog2, cat2, dog3, cat3]

for animal in animal_list:
    animal.speak()
    print(animal.info())

# cat.__created()
# print(cat.get_age())
# print(address1.city)

# cat.set_age(9)
# address1.city = "Bishkek"

# print(cat.get_age())
# print(address1.city)
# cat.info()
# cat.set_age(0)
# cat.info()


class Cow:
    def __init__(self) -> None:
        pass

    def calculate_area(self):
        pass
