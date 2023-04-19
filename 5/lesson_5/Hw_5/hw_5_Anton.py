import random
from time import sleep

from decouple import config
my_money = config("MY_MONEY")
# global my_money
# my_money = 1000
prodolgenie = True
list_of_numbers = []
for i in range(1,31):
 list_of_numbers.append(i)
# print(list_of_numbers)

def play(my_money= int(config("MY_MONEY"))):
   print(type(my_money))
   cell = int(input("Введите номер ячейки рулетки (от 1 до 30), на которую хотите сделать ставку: "))
   bet = int(input("Сколько хотите поставить?..."))
   print(f"Сделана ставка {bet} на число {cell}, ставок больше нет!")
   while True:
      win_cell = random.choice(list_of_numbers)
      print(f"Выиграла ячейка {win_cell}")
      if cell == win_cell:
         my_money += bet*2
         print("Вы выиграли!")
      else:
         my_money -= bet
         print("Вы проиграли!")
         break
   desigion = input("Хотите ли продолжить игру?... Y/N: ")
   if desigion == "Y":
      play()
   else:
      print(f"В итоге у Вас на счету: {my_money}")
    

