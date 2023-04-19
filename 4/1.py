# class Racer:
#     def drive(self):
#         print("Drive very fast")

# class Car:
#     def drive(self):
#         print("Drive")

# class RacingCar(Car,Racer):
#     pass

# car=RacingCar()
# car.drive()

class Car:
    wheels = 5

class Truck(Car):
    wheels = 10

man = Truck()
Truck.wheels = 8
kamaz = Truck()
print(man.wheels+kamaz.wheels+Car.wheels)
