# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint

def create_list(n):
    list = []
    for i in range(n):
        list.append(round(randint(0, 99) / 100 + randint(0, 9), 2))
    print(f'Список чисел: {list}')
    return list
 
def difference(some_list):
    # rounded_list = [for i round(some_list[i], 2) in some_list]
    dif_list = [round(i - int(i), 2) for i in (some_list)]
    return round((max(dif_list) - min(dif_list)), 2)

size = randint(1,10)
print(f'Искомое значение: {difference(create_list(size))}')