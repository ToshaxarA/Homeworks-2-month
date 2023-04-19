class MusicPlayMixin:
    @staticmethod
    def play_music(song):
        print(f"Играет музыка: {song}")



class Car(MusicPlayMixin):
    def __init__(self, model, year) -> None:
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, value):
        self.__year = value
    
    def drive(self):
        print("I can drive!")
    

class ElectricCar(Car):
    def __init__(self, model, year, battery) -> None:
        Car.__init__(self, model, year)
        self.__battery = battery
    
    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print("I can drive using electric engine!")

    def __str__(self) -> str:
        return f"{self.model}, {self.year}, {self.battery}"


class FuelCar(Car):
    __total_fuel = 500

    @classmethod
    def put_fuel(cls, car, amount):
        cls.__total_fuel -= amount
        car.fuel_amount += amount
        print(f"Total fuel remaind: {cls.__total_fuel}")

    @staticmethod
    def print_fuel_type():
        print("AI 98")

    def __init__(self, model, year, fuel_amount) -> None:
        Car.__init__(self, model, year)
        self.__fuel_amount = fuel_amount
    
    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, value):
        self.__fuel_amount = value

    def drive(self):  # Метод объекта
        print("I can drive using fuel engine!")

    # def info(self):
    #     print()
        
    def __str__(self) -> str:
        return f"{self.model}, {self.year}, {self.fuel_amount}"
    
    def __add__(self, other):
        object = FuelCar(
            model=self.model+other.model,
            year=self.year+other.year,
            fuel_amount=self.fuel_amount+other.fuel_amount,
            )
        return object
    
    def __sub__(self, other):
        return self.fuel_amount - other.fuel_amount
    
    def __mul__(self, other):
        return self.fuel_amount * other.fuel_amount

    def __gt__(self, other):
        return self.fuel_amount > other.fuel_amount

    def __lt__(self, other):
        return self.fuel_amount < other.fuel_amount

    def __ge__(self, other):
        return self.fuel_amount >= other.fuel_amount

    def __le__(self, other):
        return self.fuel_amount <= other.fuel_amount

    def __eq__(self, other):
        return self.fuel_amount == other.fuel_amount
    
    def __ne__(self, other):
        return self.fuel_amount != other.fuel_amount


class HybrydCar(FuelCar, ElectricCar):
    def __init__(self, model, year, battery, fuel_amount) -> None:
        ElectricCar.__init__(self, model, year, battery)
        FuelCar.__init__(self, model, year, fuel_amount)

    def __str__(self) -> str:
        return f"{self.model}, {self.year}, {self.fuel_amount}, {self.battery}"
    

hammer = FuelCar("Hammer X-super", 2015, 100)
bmw = FuelCar("bmw", 2005, 100)

tesla = ElectricCar("Tesla Mx", 2020, 80000)
prius = HybrydCar("Toyota prius", 2022, 45000, 70)


tesla.play_music("Рюмка водки")


# print(hammer)
# print(tesla)
# print(prius)

# mutant_car = prius+hammer
# print(mutant_car)
# print(hammer-bmw)
# print(hammer*bmw)
# print(hammer==bmw)

# *, /, //, +, -, **

# hammer.drive()
# tesla.drive()
# prius.drive()

# print(hammer.fuel_amount)
# FuelCar.put_fuel(hammer, 50)
# print(hammer.fuel_amount)

# print(prius.fuel_amount)
# FuelCar.put_fuel(prius, 30)
# print(prius.fuel_amount)

# FuelCar.print_fuel_type()
# hammer.print_fuel_type()

# MRO - Method Resolution Order
# print(HybrydCar.mro())
# print(HybrydCar.__mro__)
