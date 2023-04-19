
class Person:
    def __init__(self, name):
        self.name = name

    def say_my_name(self):
        print(self.name)


# print(__name__)
if __name__ == "__main__":
    p1 = Person("Baiel")
    p1.say_my_name()

