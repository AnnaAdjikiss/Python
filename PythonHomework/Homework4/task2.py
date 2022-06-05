# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:   для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from random import randint
n = randint(5,20)
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

list = [fib(e) for e in range(1,n)]

neg_list  = []
for i in list:
    neg_list.append(i)
neg_list.reverse()
for i in range(0, len(neg_list)):
    if i%2 == 0:
        neg_list[i] = neg_list[i] * -1
print(f'k = {n}')
print(f'{*neg_list, 0, *list}')