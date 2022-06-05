# Задайте два целых числа. 
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from random import randint

numberA = randint(5,20)
numberB = randint(5,20) 
max = max(numberA,numberB)
while True:
    if max % numberA == 0 and max % numberB == 0:
        print(f'НОК чисел {numberA} и {numberB}: {max}')
        break
    else:
        max += 1 
