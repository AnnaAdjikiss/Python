# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:     45 -> 101101        3 -> 11         2 -> 10

print('Введите число: ')
decimal_number = int(input())
binary_number = ''
while decimal_number > 0:
    binary_number = str(decimal_number % 2) + binary_number
    decimal_number = decimal_number // 2
print(f' В двоичной системе это будет: {binary_number}')
