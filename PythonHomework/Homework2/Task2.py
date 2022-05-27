# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:     пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n):
    number = 1
    numbers = []
    for i in range(1, n + 1):
        number *= i
        numbers.append(number)
    return numbers

print('Введите N (целое число больше 0): ')
value_N = int(input())
print(f'Набор произведений чисел от 1 до N:{factorial(value_N)}')
