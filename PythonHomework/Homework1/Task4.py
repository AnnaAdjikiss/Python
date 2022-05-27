# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:     A (3,6); B (2,1) -> 5,09            A (7,-5); B (1,-1) -> 7,21

print('Введите координату Х первой точки: ')
value_x1 = float(input())
print('Введите координату У первой точки: ')
value_y1 = float(input())

print('Введите координату Х второй точки: ')
value_x2 = float(input())
print('Введите координату У второй точки: ')
value_y2 = float(input())

import math
distance = round((math.sqrt(math.pow((value_x2 - value_x1),2) + math.pow((value_y2 - value_y1),2))),2)
print(f'Расстояние между точками: {distance}')