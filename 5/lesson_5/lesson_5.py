# 1) import random
# 2) from random import *
# 3) from random import randint

# Встроеные модули: random, time, datetime, math, os
# Кастомный модули: person, calculator
# Внешние модули / библиотеки: termcolor 

# from person import Person
# import calculator

# p1 = Person("Esen")
# p1.say_my_name()

# s = calculator.addition(9, 2)
# print(s)



# from termcolor import colored, cprint

# cprint('Hello', color='red', on_color="on_blue", 
#        attrs=["bold", "underline"])

from decouple import config

secret_key = config("SECRET_KEY", default="HAHAHAH")
password = config("PASSWORD", cast=int)

print(type(secret_key), secret_key)
print(type(password), password)
