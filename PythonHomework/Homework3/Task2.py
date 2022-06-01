# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

#  Пример:  [2, 3, 4, 5, 6] => [12, 15, 16];            [2, 3, 5, 6] => [12, 15]

from random import randint

def pairs_multiplied(some_list):
    result = []
    while len(some_list) > 1:
        result.append(some_list[0]*some_list[-1])
        del some_list[0] 
        del some_list[-1] 
    if len(some_list) ==1: result.append(some_list[0]**2)       
    return result
    
size = randint(1,10)
list = [randint(-10, 10) for i in range(size)]
print(f'Исходный список (из случайных чисел от -10 до 10): {list}')
print(f'Результирующий список: {pairs_multiplied(list)}')