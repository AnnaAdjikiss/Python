# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

from random import randint

def list_of_uniques(args):
    uniques = [i for i in args if args.count(i) == 1]
    return uniques
    

list = [randint(0, 10) for i in range(randint(5, 15))] 
print(f' Дана последовательность: {list}')
# list = [1, 2, 3, 5, 1, 5, 3, 10]
print(f' Cписок уникальных элементов: {list_of_uniques(list)}')
