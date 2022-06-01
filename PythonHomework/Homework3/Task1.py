# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
 
def create_list(n):
    list = []
    for i in range(n):
        list.append(randint(1,11))
    print(f'Список чисел: {list}')
    return list

def sum_odd_elem(some_list):
    sum = 0
    for i in range(0, len(some_list)):
        if (i%2 != 0):
            sum = sum + some_list[i]
    return sum

size = randint(5,11)
print(f'Сумма эл-тов с нечетным индексом: {sum_odd_elem(create_list(size))}')
