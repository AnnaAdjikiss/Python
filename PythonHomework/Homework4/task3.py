# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

from random import randint

def create_string(n): 
    string = ''
    for i in range(n):
        string = string + str(randint(-99,100)) + ' '
    print(f'строка: {string}')
    return string

list_of_numbers = [int(i) for i in create_string(randint(5,20)).split()]

print(f'меньшее число: {min(list_of_numbers)}, большее число: {max(list_of_numbers)}')
