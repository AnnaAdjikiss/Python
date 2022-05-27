# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр(отсекаем минус, считаем все в плюс).
# Пример:       67,82 -> 23         0,56 -> 11

print('Введите вещественное число: ')
number = input()
result = 0
for i in range(len(number)):
    if (number[i] != '-' and number[i] != '.'):
        result = result + int(number[i])
print(f'Сумма цифр в числе {number} равна {result}')